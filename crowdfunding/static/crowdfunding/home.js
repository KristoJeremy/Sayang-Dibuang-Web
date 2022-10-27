// handling the nav tabs
const showCrowdfundingById = (pk) => {
  window.location = `${pk}`;
};

const getCrowdfunds = (userOnly = false, userId = null) => {
  fetch("/crowdfundings/json")
    .then((res) => res.json())
    .then((crowdfunds) => {
      const crowdfundSection = document.querySelector("#crowdfunds");
      if (userOnly) {
        crowdfunds = crowdfunds.filter((c) => c.fields.user === userId);
      }
      crowdfunds.map((crowdfund) => {
        // fetching user that posted the crowdfund
        fetch(`/crowdfundings/get-user-by-id/${crowdfund.fields.user}`)
          .then((res) => res.json())
          .then((data) => {
            const user = data;

            // formatting date of crowdfund
            const date = new Date(`${crowdfund.fields.created}`);
            const formattedDate = new Intl.DateTimeFormat("id-ID", {
              dateStyle: "long",
              timeStyle: "short",
            }).format(date);
            crowdfundSection.insertAdjacentHTML(
              "afterbegin",
              `<div id="crowdfund-${crowdfund.pk}" class="crowdfund card mb-5">
                  <div class="card-header d-flex justify-items-center align-items-center gap-2">
                      <img
                      onclick="showCrowdfundingById(${crowdfund.pk})"
                        class="rounded-circle"
                        style="width: 50px"
                        src="https://www.kindpng.com/picc/m/171-1712282_profile-icon-png-profile-icon-vector-png-transparent.png"
                        alt=""
                      />
                      <div>
                        <strong>${user.username}</strong>
                        <p>Ditayangkan ${formattedDate}</p>
                      </div>
                  </div>
                  <div class="card-body">
                      <h2 class="card-title" style="font-family:Verona; ">${
                        crowdfund.fields.title
                      }</h2>

                      <p class="card-text">
                        ${crowdfund.fields.description}
                      </p>

                      <div class="progress mb-3">
                        <div
                            class="progress-bar bg-success progress-bar-striped progress-bar-animated"
                            role="progressbar"
                            style="width: ${
                              (crowdfund.fields.received /
                                crowdfund.fields.target) *
                              100
                            }%"
                          >
                            ${crowdfund.fields.received} dari
                            ${crowdfund.fields.target} benda diperoleh
                        </div>
                      </div>
              
                      <div class="d-flex justify-content-end">
                      ${
                        !userOnly
                          ? `<button
                              type="button"
                              class="btn btn-sand border"
                              data-bs-toggle="modal"
                              data-bs-target="#contact-modal-${crowdfund.fields.user}"
                            >
                              Bantu ${user.username}
                            </button>`
                          : `<div>
                              <a
                                type="button"
                                class="btn btn-outline-dark-green"
                                href="/crowdfundings/edit/${crowdfund.pk}"
                                >
                                Ubah
                              </a>
                              <button
                                type="button"
                                class="btn btn-outline-danger"
                                data-bs-toggle="modal"
                                data-bs-target="#delete-modal-${crowdfund.pk}"
                                >
                                Hapus
                              </button>
                        </div>`
                      }
                  
                      <div
                        class="modal fade"
                        id="contact-modal-${crowdfund.fields.user}"
                        tabindex="-1"
                        aria-labelledby="contactModalLabel"
                        aria-hidden="true"
                      >
                          <div class="modal-dialog">
                              <div class="modal-content">
                                  <div class="modal-header">
                                      <h5 class="modal-title" id="exampleModalLabel">
                                        ${user.full_name}
                                      </h5>
                                      <button
                                        type="button"
                                        class="btn-close"
                                        data-bs-dismiss="modal"
                                        aria-label="Close"
                                      ></button>
                                  </div>
            
                                <div class="modal-body">
                                    <div class="d-flex gap-2">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
                                        <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                                        </svg>
                                        <p>${user.whatsapp}</p>
                                    </div>
                                    <p>
                                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16">
                                      <path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
                                      </svg>
                                      ${user.whatsapp}
                                    </p>
                                    <p>${user.line}</p>
                                </div>
                                
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-primary">
                                      Contact ${user.username}
                                    </button>
                                </div>
                              </div>
                          </div>
                      </div>

                      <div
                        class="modal fade"
                        id="delete-modal-${crowdfund.pk}"
                        tabindex="-1"
                        aria-labelledby="contactModalLabel"
                        aria-hidden="true"
                      >
                          <div class="modal-dialog">
                              <div class="modal-content">
                                  <div class="modal-header">
                                      <h5 class="modal-title" id="exampleModalLabel">
                                        Menghapus Crowdfund
                                      </h5>
                                      <button
                                        type="button"
                                        class="btn-close"
                                        data-bs-dismiss="modal"
                                        aria-label="Close"
                                      ></button>
                                  </div>
              
                                  <div class="modal-body">
                                      <p>Apakah kamu yakin ingin menghapus crowdfund ini?</p>
                                      <div class="d-flex justify-content-end">
                                        <button type="button" class="btn btn-outline-danger" onclick="deleteCrowdfund(${
                                          crowdfund.pk
                                        })">
                                          Hapus
                                        </button>
                                      </div>
                              </div>
                          </div>
                      </div>

                    </div>

                    </div>
                </div>`
            );
          })
          .catch((err) => console.log(err));
      });
    })
    .catch((err) => console.log(err));
};

const getUserCrowdfunds = (pk) => {
  getCrowdfunds(true, pk);
};

const removeCrowdfunds = () => {
  const crowdfund = document.querySelectorAll(".crowdfund");
  crowdfund.forEach((c) => c.remove());
};

const deleteCrowdfund = (id) => {
  fetch(`/crowdfundings/delete/${id}`, {
    method: "DELETE",
    headers: {
      "X-CSRFToken": window.csrftoken,
    },
  }).then((res) => {
    const crowdfundToBeRemoved = document.querySelector(`#crowdfund-${id}`);
    const deleteModalElement = document.querySelector(`#delete-modal-${id}`);
    const deleteModal = bootstrap.Modal.getInstance(deleteModalElement);
    deleteModal.hide();
    crowdfundToBeRemoved.remove();
  });
};

window.onload = () => {
  // changing style of navbar on scroll
  // reference: https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling
  const navbar = document.querySelector(".navbar");
  window.onscroll = () => {
    if (window.scrollY > 100) {
      navbar.classList.add("bg-sand");
    } else {
      navbar.classList.remove("bg-sand");
    }
  };

  // getting all crowdfunds
  getCrowdfunds();

  // handling nav toggles
  let allSelected = true;
  const allCrowdfundsBtn = document.querySelector("#all-crowdfunds-btn");
  const myCampaignBtn = document.querySelector("#my-campaign-btn");
  const addBtn = document.querySelector("#add-btn");

  allCrowdfundsBtn.addEventListener("click", () => {
    if (!allSelected) {
      allSelected = true;
      // change state of button
      allCrowdfundsBtn.classList.remove("text-brown");
      allCrowdfundsBtn.classList.add("bg-brown");
      allCrowdfundsBtn.classList.add("text-white");
      myCampaignBtn.classList.remove("bg-brown");
      myCampaignBtn.classList.remove("text-white");
      myCampaignBtn.classList.add("text-brown");

      // change the cards being displayed
      removeCrowdfunds();
      getCrowdfunds();

      // hide add button
      addBtn.classList.add("d-none");
    }
  });

  myCampaignBtn.addEventListener("click", () => {
    allSelected = false;
    // change state of button
    myCampaignBtn.classList.remove("text-brown");
    myCampaignBtn.classList.add("bg-brown");
    myCampaignBtn.classList.add("text-white");
    allCrowdfundsBtn.classList.remove("bg-brown");
    allCrowdfundsBtn.classList.remove("text-white");
    allCrowdfundsBtn.classList.add("text-brown");

    // change cards being displayed is handled by the onclick attribute of the button

    // show add button
    addBtn.classList.remove("d-none");
  });
};
