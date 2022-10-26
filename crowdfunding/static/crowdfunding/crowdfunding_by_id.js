window.onload = () => {
  // getting the crowdfund ID
  const id = window.location.pathname.split("/")[2];

  // fetching the data
  fetch(`/crowdfundings/json/${id}`)
    .then((res) => res.json())
    .then((data) => {
      const crowdfund = data[0];
      console.log(crowdfund);

      // getting user that posted the crowdfund
      fetch(`/crowdfundings/get-user-by-id/${crowdfund.fields.user}`)
        .then((res) => res.json())
        .then((data) => {
          const user = data;
          // inserting data to page
          const crowdfundSection = document.querySelector("#crowdfund");
          crowdfundSection.insertAdjacentHTML(
            "beforeend",
            `<div>
                <h1>${crowdfund.fields.title}</h1>
                <div>${crowdfund.fields.description}</div>
            </div>`
          );
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
};
