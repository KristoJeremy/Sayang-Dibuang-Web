$(document).ready(function() {
    var data

    // GET data profil user
    $.ajax({
        url: window.getUrl,
        type: "GET",
        success: function(response) {
            console.log(response)
            data = response[0].fields

            // Set nomor telepon
            $("#id_telephone").attr("disabled", "disabled")
            $("#id_telephone").val(data.telephone !== "" ? data.telephone : "-")
            
            // Set nomor whatsapp
            $("#id_whatsapp").attr("disabled", "disabled")
            $("#id_whatsapp").val(data.whatsapp !== "" ? data.whatsapp : "-")

            // Set ID line
            $("#id_line").attr("disabled", "disabled")
            $("#id_line").val(data.line !== "" ? data.line : "-")
        }
    })
    // Set username dan email
    $("#username").val(window.username)
    $("#email").val(window.email)

    // Set nama depan dan nama belakang
    $("#id_first_name").attr("disabled", "disabled")
    $("#id_first_name").val(window.firstName)

    $("#id_last_name").attr("disabled", "disabled")
    $("#id_last_name").val(window.lastName)
    

    // Menambahkan dan menghapus tombol update
    var change = false
    var jumlah_element_input = 7

    $("button.profile").click(function(){
        $("div.alert-success").remove()
        if ($(this).siblings().attr("disabled") === "disabled") {
            $(this).siblings().removeAttr("disabled")
            $(this).text("Cancel")
            $(this).removeClass("bg-dark-green")
            $(this).addClass("bg-gold")

            if (change === false) {                
                $("form").append(`
                <div class="d-grid gap-2 col-12 mx-auto update">
                    <input class="btn btn-gold text-sand center m-3" type="submit" name="submit" value="Update" class="update">
                </div>
                `)
                change = true
            }
        } else {
            $(this).siblings().attr("disabled", "disabled")
            $(this).text("Change")

            $(this).removeClass("bg-gold")
            $(this).addClass("bg-dark-green")

            var buttonId = $(this).attr("id")
            
            // Ubah value input ke awal ketika tombol Cancel ditekan
            if (buttonId === "change-name") {
                // Set nama depan dan nama belakang
                $("#id_first_name").val(window.firstName)
                $("#id_last_name").val(window.lastName)
            } else if (buttonId  === "change-telephone") {
                $("#id_telephone").val(data.telephone !== "" ? data.telephone : "-")
                $("p.telephone-message").remove()
            } else if (buttonId  === "change-whatsapp") {
                $("#id_whatsapp").val(data.whatsapp !== "" ? data.whatsapp : "-")
                $("p.whatsapp-message").remove()
            } else if (buttonId === "change-line") {
                $("#id_line").val(data.line !== "" ? data.line : "-")
            }

            // $("[disabled=disabled]").length untuk menghilangkan tombol update
            if ($("[disabled=disabled]").length === jumlah_element_input) {
                $("form").children("div.update").remove()
                change = false
            }
        }
    })
    
    $("form#update-profile").submit(function(e) {
        e.preventDefault()

        $.ajax({
            type: "POST",
            url: window.postUrl,
            data: $(this).serialize(),
            success: function(response){
                console.log("success")

                // disable semua input dan mengubah semua warna
                $("input").attr("disabled", "disabled")
                $("button.profile").removeClass("bg-gold")
                $("button.profile").addClass("bg-dark-green")

                // Menghilangkan tombol update
                $("form").children("div.update").remove()

                // Menghapus pesan (jika ada)
                $("p.telephone-message").remove()
                $("p.whatsapp-message").remove()

                // Mengubah text button
                var buttons = $("button.profile")
                for (const key in buttons) {
                    if (Object.hasOwnProperty.call(buttons, key)) {
                        const element = buttons[key];

                        if (element.textContent === "Cancel") {
                            element.textContent = "Change"
                        }
                    }
                }
                
                // Set change
                change = false

                // Set CSRF untuk perubahan selanjutnya
                $("[name=csrfmiddlewaretoken]").removeAttr("disabled")
                $("div.card-body").append(`
                <div class="alert alert-success" role="alert">
                    <div class="d-flex justify-content-between">
                        <span>Perubahan berhasil!</span> 
                        <button type="button" class="btn-close float-right" aria-label="Close"></button>
                    </div>
                </div>
                `)

                console.log($("button.btn-close"))
                
                $("button.btn-close").click(function(){
                    $("div.alert-success").remove()
                })
            },
            error: function(response) {
                console.log("error")

                var json_response = JSON.parse(response.responseJSON)

                for (const key in json_response) {
                    if (Object.hasOwnProperty.call(json_response, key)) {
                        const element = json_response[key][0];
                        
                        if (key === "telephone") {
                            if ($("div.telephone").children().length === 1) {
                                $("div.telephone").append(`<p class="telephone-message">${element.message}</p>`)
                            }
                        } else if (key === "whatsapp") {
                            if ($("div.whatsapp").children().length === 1) {
                                $("div.whatsapp").append(`<p class="whatsapp-message">${element.message}</p>`)
                            }
                        }
                    }
                }

                // Hapus message untuk field yang sudah valid
                if (!json_response.hasOwnProperty("telephone") && $("div.telephone").children().length == 2) {
                    $("p.telephone-message").remove()
                } else if (!json_response.hasOwnProperty("whatsapp") && $("div.whatsapp").children().length === 2) {
                    $("p.whatsapp-message").remove()
                }
            }
        })
    })
})