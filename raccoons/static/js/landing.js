const title = document.getElementById('raccoons-title');

function getRandomHackerTitle() {
  const fontStyle = Math.floor(Math.random() * (8 - 1)) + 1;
  let titleString;
  switch (fontStyle) {
    case 1: titleString = 'Raccoons H4ck3r Clu6'; break;
    case 2: titleString = 'Raccoons Hacker Clu6'; break;
    case 3: titleString = 'Raccoons H4ck3r Club'; break;
    case 4: titleString = 'R4cc00n5 Hacker Club'; break;
    case 5: titleString = 'R4cc00n5 Hacker Clu6'; break;
    case 6: titleString = 'R4cc00n5 H4ck3r Club'; break;
    case 7: titleString = 'R4cc00n5 H4ck3r Clu6'; break;
  }
  title.innerHTML = titleString;
}

function getNormalizedTitle() {
  title.innerHTML = "Raccoons Hacker Club"
}

title.addEventListener("mouseover", getRandomHackerTitle);
title.addEventListener("mouseleave", getNormalizedTitle);

window.setInterval(() => {
  getRandomHackerTitle();
  setTimeout(getNormalizedTitle, 250);
}, 4000);

