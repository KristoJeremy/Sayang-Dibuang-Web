// handling the nav tabs
window.onload = () => {
  const allCrowdfundsBtn = document.querySelector("#all-crowdfunds-btn");
  const myCampaignBtn = document.querySelector("#my-campaign-btn");

  allCrowdfundsBtn.addEventListener("click", () => {
    // change state of button
    allCrowdfundsBtn.classList.add("active");
    myCampaignBtn.classList.remove("active");

    // change the cards being displayed
  });

  myCampaignBtn.addEventListener("click", () => {
    // change state of button
    myCampaignBtn.classList.add("active");
    allCrowdfundsBtn.classList.remove("active");

    // change the cards being displayed
  });
};
