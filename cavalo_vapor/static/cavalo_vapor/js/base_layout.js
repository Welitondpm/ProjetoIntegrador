var modo = 1
function showMenu() {
  if (modo == 1) {
    document.getElementById('cobreatela').style.display = 'flex';
    document.getElementById('colorpickers').style.display = 'flex';
    modo--
  } else {
    document.getElementById('cobreatela').style.display = 'none';
    document.getElementById('colorpickers').style.display = 'none';
    modo++
  }
}

var modo2 = 1
function showFiltros() {
  if (modo2 == 1) {
    document.getElementById('filtrar').style.display = 'flex';
    modo2--
  } else {
    document.getElementById('filtrar').style.display = 'none';
    modo2++
  }
}

function cor() {
  let cor = hexToRgb(document.getElementById("cor").value)
  let oposta = rgbToHex(255 - cor.r, 255 - cor.g, 255 - cor.b)
  let ter1 = rgbToHex(cor.b, cor.r, cor.g)
  let ter2 = rgbToHex(cor.g, cor.b, cor.r)
  let quat1 = rgbToHex((cor.r + (255 - cor.r)) * .25, (cor.g + (255 - cor.g)) * .25, (cor.b + (255 - cor.b)) * .25)
  let quat2 = rgbToHex((cor.r + (255 - cor.r)) * .75, (cor.g + (255 - cor.g)) * .75, (cor.b + (255 - cor.b)) * .75)
  document.querySelector(':root').style.setProperty('--cor', cor);
  document.querySelector(':root').style.setProperty('--oposta', oposta);
  document.querySelector(':root').style.setProperty('--ter1', ter1);
  document.querySelector(':root').style.setProperty('--ter2', ter2);
  document.querySelector(':root').style.setProperty('--quat1', quat1);
  document.querySelector(':root').style.setProperty('--quat2', quat2);
}

function hexToRgb(hex) {
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}

function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}