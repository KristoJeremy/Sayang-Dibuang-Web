// handling the nav tabs
const showCrowdfundingById = (pk) => {
  window.location = `${pk}`;
};

const getCrowdfunds = ({ userOnly = false, userId = null } = {}) => {
  fetch("/crowdfundings/json")
    .then((res) => res.json())
    .then((crowdfunds) => {
      const crowdfundSection = document.querySelector("#crowdfunds");
      if (userOnly) {
        crowdfunds = crowdfunds.filter((c) => c.user_id == userId);
      }
      crowdfunds.map((crowdfund) => {
        // formatting date of crowdfund
        const date = new Date(`${crowdfund.created}`);
        const formattedDate = new Intl.DateTimeFormat("id-ID", {
          dateStyle: "long",
          timeStyle: "short",
        }).format(date);

        // trimming the description into only the text
        // source: https://stackoverflow.com/questions/822452/strip-html-from-text-javascript
        let trimmedDescription = crowdfund.description.replace(
          /<\/?("[^"]*"|'[^']*'|[^>])*(>|$)/g,
          ""
        );

        // getting the first 50 words of the description
        // source: https://stackoverflow.com/questions/29126888/what-is-the-best-way-to-get-the-first-x-number-of-words-from-a-string-javascript
        fiftyWordsDescription = trimmedDescription
          .split(/\s+/)
          .slice(0, 50)
          .join(" ");

        // adding three dots if the description is too long
        if (trimmedDescription.length > fiftyWordsDescription.length) {
          fiftyWordsDescription += "...";
        }

        // inserting cards
        crowdfundSection.insertAdjacentHTML(
          "beforebegin",
          `<div id="crowdfund-${crowdfund.id}" class="crowdfund card mb-5">
              <div class="card-header d-flex justify-items-center align-items-center gap-2">
                  <img
                    class="rounded-circle"
                    style="width: 50px"
                    src="https://www.kindpng.com/picc/m/171-1712282_profile-icon-png-profile-icon-vector-png-transparent.png"
                    alt=""
                  />
                  <div>
                    <strong>${crowdfund.profile.user.username}</strong>
                    <p>Ditayangkan ${formattedDate}</p>
                  </div>
              </div>
              <div class="card-body">
                  <div id="card-view-all-btn" class="mb-3" onclick="showCrowdfundingById(${
                    crowdfund.id
                  })">
                      <h2 class="card-title" style="font-family:Verona; ">${
                        crowdfund.title
                      }</h2>
                      
                      <p class="card-text">
                      ${fiftyWordsDescription}
                      </p>
                  
                  </div>
                  <div class="progress mb-3">
                    <div
                        class="progress-bar bg-success progress-bar-striped progress-bar-animated"
                        role="progressbar"
                        style="width: ${
                          (crowdfund.received / crowdfund.target) * 100
                        }%"
                      >
                        ${crowdfund.received} dari
                        ${crowdfund.target} benda diperoleh
                    </div>
                  </div>
          
                  <div class="d-flex justify-content-end">
                  ${
                    crowdfund.user_id != userId
                      ? `<div>
                      <a
                          class="btn btn-sand border"
                          data-bs-toggle="modal"
                          data-bs-target="#contact-modal-${crowdfund.user_id}"
                        >
                          Bantu ${crowdfund.profile.user.first_name}
                        </a>
                        ${
                          crowdfund.description > trimmedDescription
                            ? `<a
                            class="btn btn-outline-dark-green ml-4"
                            onclick="showCrowdfundingById(${crowdfund.id})"
                          >
                            Baca Lebih Lanjut
                          </a>`
                            : ""
                        }
                        </div>`
                      : `<div>
                          <a
                            type="button"
                            class="btn btn-outline-dark-green"
                            href="/crowdfundings/edit/${crowdfund.id}"
                            >
                            Ubah
                          </a>
                          <button
                            type="button"
                            class="btn btn-outline-danger"
                            data-bs-toggle="modal"
                            data-bs-target="#delete-modal-${crowdfund.id}"
                            >
                            Hapus
                          </button>
                    </div>`
                  }
              
                  <div
                    class="modal fade"
                    id="contact-modal-${crowdfund.user_id}"
                    tabindex="-1"
                    aria-labelledby="contactModalLabel"
                    aria-hidden="true"
                  >
                      <div class="modal-dialog">
                          <div class="modal-content">
                              <div class="modal-header">
                                  <h4 class="mb-2 fw-bold">${
                                    crowdfund.profile.user.first_name +
                                    " " +
                                    crowdfund.profile.user.last_name
                                  }</h4>
                                  <button
                                        type="button"
                                        class="btn-close"
                                        data-bs-dismiss="modal"
                                        aria-label="Close"
                                  ></button>
                              </div>
                              
                              <div class="modal-body p-4 rounded mb-4">
                                    <div class="d-flex gap-3 align-items-center mb-3">
                                        <div class="flex-shrink-0">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16">
                                              <path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
                                            </svg>
                                        </div>
                                        <h5>
                                            ${crowdfund.profile.telephone}
                                        </h5>
                                    </div>
            
                                    <a
                                      class="d-flex gap-3 align-items-center btn btn-sand mb-2"
                                      href="mailto:${
                                        crowdfund.profile.user.email
                                      }"
                                      target="_blank">
                                      <div class="flex-shrink-0">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16">
                                          <path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z"/>
                                        </svg>
                                      </div>
                                      <div>
                                        Email ${
                                          crowdfund.profile.user.first_name
                                        }
                                      </div>
                                    </a>
            
                                    ${
                                      crowdfund.profile.whatsapp != ""
                                        ? `<a
                                      class="d-flex gap-3 align-items-center btn btn-dark-green mb-2"
                                      href="https://wa.me/+62${
                                        crowdfund.profile.whatsapp.startsWith(0)
                                          ? crowdfund.profile.whatsapp.substring(
                                              1
                                            )
                                          : crowdfund.profile.whatsapp.substring(
                                              3
                                            )
                                      }"
                                      target="_blank">
                                      <div class="flex-shrink-0">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
                                          <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                                        </svg>
                                      </div>
                                      <div>
                                        WhatsApp ${
                                          crowdfund.profile.user.first_name
                                        }
                                      </div>
                                    </a>`
                                        : ""
                                    }
                                    
                                    ${
                                      crowdfund.profile.line != ""
                                        ? `<a
                                      class="d-flex gap-3 align-items-center btn btn-brown mb-2"
                                      href="https://line.me/R/ti/p/~${crowdfund.profile.line}"
                                      target="_blank"
                                    >
                                      <div class="flex-shrink-0">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-line" viewBox="0 0 16 16">
                                          <path d="M8 0c4.411 0 8 2.912 8 6.492 0 1.433-.555 2.723-1.715 3.994-1.678 1.932-5.431 4.285-6.285 4.645-.83.35-.734-.197-.696-.413l.003-.018.114-.685c.027-.204.055-.521-.026-.723-.09-.223-.444-.339-.704-.395C2.846 12.39 0 9.701 0 6.492 0 2.912 3.59 0 8 0ZM5.022 7.686H3.497V4.918a.156.156 0 0 0-.155-.156H2.78a.156.156 0 0 0-.156.156v3.486c0 .041.017.08.044.107v.001l.002.002.002.002a.154.154 0 0 0 .108.043h2.242c.086 0 .155-.07.155-.156v-.56a.156.156 0 0 0-.155-.157Zm.791-2.924a.156.156 0 0 0-.156.156v3.486c0 .086.07.155.156.155h.562c.086 0 .155-.07.155-.155V4.918a.156.156 0 0 0-.155-.156h-.562Zm3.863 0a.156.156 0 0 0-.156.156v2.07L7.923 4.832a.17.17 0 0 0-.013-.015v-.001a.139.139 0 0 0-.01-.01l-.003-.003a.092.092 0 0 0-.011-.009h-.001L7.88 4.79l-.003-.002a.029.029 0 0 0-.005-.003l-.008-.005h-.002l-.003-.002-.01-.004-.004-.002a.093.093 0 0 0-.01-.003h-.002l-.003-.001-.009-.002h-.006l-.003-.001h-.004l-.002-.001h-.574a.156.156 0 0 0-.156.155v3.486c0 .086.07.155.156.155h.56c.087 0 .157-.07.157-.155v-2.07l1.6 2.16a.154.154 0 0 0 .039.038l.001.001.01.006.004.002a.066.066 0 0 0 .008.004l.007.003.005.002a.168.168 0 0 0 .01.003h.003a.155.155 0 0 0 .04.006h.56c.087 0 .157-.07.157-.155V4.918a.156.156 0 0 0-.156-.156h-.561Zm3.815.717v-.56a.156.156 0 0 0-.155-.157h-2.242a.155.155 0 0 0-.108.044h-.001l-.001.002-.002.003a.155.155 0 0 0-.044.107v3.486c0 .041.017.08.044.107l.002.003.002.002a.155.155 0 0 0 .108.043h2.242c.086 0 .155-.07.155-.156v-.56a.156.156 0 0 0-.155-.157H11.81v-.589h1.525c.086 0 .155-.07.155-.156v-.56a.156.156 0 0 0-.155-.157H11.81v-.589h1.525c.086 0 .155-.07.155-.156Z"/>
                                        </svg>
                                      </div>
                                      <div>
                                        LINE ${crowdfund.profile.user.first_name}
                                      </div>
                                    </a>`
                                        : ""
                                    }
                                </div>
                            
                              </div>
                        </div>
                  </div>

                  <div
                    class="modal fade"
                    id="delete-modal-${crowdfund.id}"
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
                                      crowdfund.id
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
      });
    })
    .catch((err) => console.log(err));
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

const allCrowdfundsSelected = () => {
  if (!allSelected) {
    removeCrowdfunds();
    getCrowdfunds({ userId: loggedInId });
  }
};

const myCampaignsSelected = () => {
  if (allSelected) {
    removeCrowdfunds();
    getCrowdfunds({ userOnly: true, userId: loggedInId });
  }
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

  // handling nav toggles
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
