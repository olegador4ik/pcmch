function countQ(a, b) {
  let h = 0;
  let j = 0;
  switch(a) {
    case 0:
      h = h + b;
      return [h, j];
    case 1:
      h = h - b;
      return [h, j];
    case 2:
      j = j - b;
      return [h, j];
    case 3:
      j = j + b;
      return [h, j];
    };
}

function endQ(a, b) {
  window.location.href = "/result";
  sessionStorage.setItem("t", a);
  sessionStorage.setItem("e", b);
}

function tgth() {
  if (document.documentElement.getAttribute('data-theme') === 'dark') {
    document.documentElement.setAttribute('data-theme', 'light');
    sessionStorage.setItem("theme", "light");
  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    sessionStorage.setItem("theme", "dark");
  }
}
