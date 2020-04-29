
function update_bars(evnt){

  var c1 = document.getElementById('circle1').innerHTML;
  var c2 = document.getElementById('circle2').innerHTML;
  var c3 = document.getElementById('circle3').innerHTML;
  var c4 = document.getElementById('circle4').innerHTML;
  var c5 = document.getElementById('circle5').innerHTML;

  var maxC = Math.max(c1,c2,c3,c4,c5);

  function barHeight(bar) {
    return (((bar / maxC) * 100 ) * 2);
  }

  function marTop(barH) {
    return ((barH-2)*-1)
  }

  var c1h = barHeight(c1)
  var c2h = barHeight(c2)
  var c3h = barHeight(c3)
  var c4h = barHeight(c4)
  var c5h = barHeight(c5)
  var c1m = marTop(c1h)
  var c2m = marTop(c2h)
  var c3m = marTop(c3h)
  var c4m = marTop(c4h)
  var c5m = marTop(c5h)

  if (c1h > 17) {
    var C1Label = 16
  } else {
    var C1Label = 0
  };
  if (c2h > 17) {
    var C2Label = 16
  } else {
    var C2Label = 0
  };
  if (c3h > 17) {
    var C3Label = 16
  } else {
    var C3Label = 0
  };
  if (c4h > 17) {
    var C4Label = 16
  } else {
    var C4Label = 0
  };
  if (c5h > 17) {
    var C5Label = 16
  } else {
    var C5Label = 0
  };

  var objc1 = document.querySelector('.circle1');
  var objc2 = document.querySelector('.circle2');
  var objc3 = document.querySelector('.circle3');
  var objc4 = document.querySelector('.circle4');
  var objc5 = document.querySelector('.circle5');
  var axis = document.getElementById('axis1')

  oldh1 = objc1.offsetHeight;
  oldh2 = objc2.offsetHeight;
  oldh3 = objc3.offsetHeight;
  oldh4 = objc4.offsetHeight;
  oldh5 = objc5.offsetHeight;

  oldm1 = marTop(oldh1)
  oldm2 = marTop(oldh2)
  oldm3 = marTop(oldh3)
  oldm4 = marTop(oldh4)
  oldm5 = marTop(oldh5)

  objc1.style.animation = 'none';
  objc1.offsetHeight;
  objc1.style.animation = null;

  objc2.style.animation = 'none';
  objc2.offsetHeight;
  objc2.style.animation = null;

  objc3.style.animation = 'none';
  objc3.offsetHeight;
  objc3.style.animation = null;

  objc4.style.animation = 'none';
  objc4.offsetHeight;
  objc4.style.animation = null;

  objc5.style.animation = 'none';
  objc5.offsetHeight;
  objc5.style.animation = null;

  function addAnimationC1(keys) {
    // document.head.removeChild(stylec1
    var sheet = document.getElementById('stylec1');
    sheet.disabled = true;
    sheet.parentNode.removeChild(sheet);
    sheet.classList.remove("run-animation");
    var stylec1 = document.createElement('style');
    stylec1.type = 'text/css';
    stylec1.id = 'stylec1';
    document.head.appendChild(stylec1);
    stylec1.sheet.insertRule(keys, stylec1.length);
  }
  addAnimationC1(`
    @keyframes barometize {
      0%  { position: absolute; transform: translate(0%, 0%); height: `+ oldh1 +`px; margin-top:` + oldm1 + `px; border-radius: 1%; font-size: ` + C1Label + `px; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 1%; font-size: 0; margin-top: 0px;}
      30% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; font-size: 0 }
      50% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      60% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      65% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      70% { height: 50px; transform: translate(0%, 0%); border-radius: 10%; margin-top: 0px; }
      85% { height: `+ c1h +`px; margin-top: ` + c1m + `px; font-size: 0px; }
      100% { position: absolute; height: `+ c1h +`px; margin-top:` + c1m + `px; border-radius: 1%; font-size: ` + C1Label + `px; }
    }
  `);

  function addAnimationC2(keys) {
    var sheet2 = document.getElementById('stylec2');
    sheet2.disabled = true;
    sheet2.parentNode.removeChild(sheet2);
    sheet2.classList.remove("barometize2");
    var stylec2 = document.createElement('style');
    stylec2.type = 'text/css';
    stylec2.id = 'stylec2';
    document.head.appendChild(stylec2);
    stylec2.sheet.insertRule(keys, stylec2.length);
    sheet2.classList.add("run-animation");
  }
  addAnimationC2(`
    @keyframes barometize2 {
      0%  { position: absolute; transform: translate(110%, 0%); height: `+ oldh2 +`px; margin-top:` + oldm2 + `px;  border-radius: 1%; font-size: ` + C2Label + `px; }
      20% { height: 50px; transform: translate(110%, 0%); border-radius: 1%; font-size: 0; margin-top: 0px;}
      30% { height: 50px; transform: translate(110%, 0%); border-radius: 100%; font-size: 0 }
      50% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      60% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      65% { height: 50px; transform: translate(110%, 0%); border-radius: 100%; }
      70% { height: 50px; transform: translate(110%, 0%); border-radius: 10%; margin-top: 0px; }
      82% { transform: translate(110%, 0%); height: `+ c2h +`px; margin-top: ` + c2m + `px; font-size: 0px; }
      100% { transform: translate(110%, 0%); height: `+ c2h +`px; margin-top:` + c2m + `px; border-radius: 1%; font-size: ` + C2Label + `px; }
    }
  `);

  function addAnimationC3(keys) {
    var sheet3 = document.getElementById('stylec3');
    sheet3.disabled = true;
    sheet3.parentNode.removeChild(sheet3);
    sheet3.classList.remove("run-animation");
    var stylec3 = document.createElement('style');
    stylec3.type = 'text/css';
    stylec3.id = 'stylec3';
    document.head.appendChild(stylec3);
    stylec3.sheet.insertRule(keys, stylec3.length);
  }
  addAnimationC3(`
    @keyframes barometize3 {
      0% { position: absolute; height: 50px; border-radius: 1%; transform: translate(220%, 0%); height: `+ oldh3 +`px; margin-top:` + oldm3 + `px; font-size: ` + C3Label + `px;}
      20% { height: 50px; transform: translate(220%, 0%); border-radius: 1%; font-size: 0; margin-top: 0px;}
      30% { height: 50px; transform: translate(220%, 0%); border-radius: 100%; font-size: 0 }
      50% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      60% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      65% { height: 50px; transform: translate(220%, 0%); border-radius: 100%; }
      70% { height: 50px; transform: translate(220%, 0%); border-radius: 10%; margin-top: 0px; }
      80% { transform: translate(220%, 0%); height: `+ c3h +`px; margin-top: ` + c3m + `px;  font-size: 0px;}
      100% { transform: translate(220%, 0%); height: `+ c3h +`px; margin-top:` + c3m + `px; border-radius: 1%; font-size: ` + C3Label + `px; }
    }
  `);

  function addAnimationC4(keys) {
    var sheet4 = document.getElementById('stylec4');
    sheet4.disabled = true;
    sheet4.parentNode.removeChild(sheet4);
    sheet4.classList.remove("run-animation");
    var stylec4 = document.createElement('style');
    stylec4.type = 'text/css';
    stylec4.id = 'stylec4';
    document.head.appendChild(stylec4);
    stylec4.sheet.insertRule(keys, stylec4.length);
  }
  addAnimationC4(`
    @keyframes barometize4 {
      0% { position: absolute; height: 50px; border-radius: 1%; transform: translate(330%, 0%); height: `+ oldh4 +`px; margin-top:` + oldm4 + `px; font-size: ` + C4Label + `px;}
      20% { height: 50px; transform: translate(330%, 0%); border-radius: 1%; font-size: 0; margin-top: 0px;}
      30% { height: 50px; transform: translate(330%, 0%); border-radius: 100%; font-size: 0 }
      50% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      60% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      65% { height: 50px; transform: translate(330%, 0%); border-radius: 100%; }
      70% { height: 50px; transform: translate(330%, 0%); border-radius: 10%; margin-top: 0px; }
      82% { transform: translate(330%, 0%); height: `+ c4h +`px; margin-top: ` + c4m + `px; font-size: 0px; }
      100% { transform: translate(330%, 0%); height: `+ c4h +`px; margin-top:` + c4m + `px; border-radius: 1%;  font-size: ` + C4Label + `px;}
    }
  `);

  function addAnimationC5(keys) {
    var sheet5 = document.getElementById('stylec5');
    sheet5.disabled = true;
    sheet5.parentNode.removeChild(sheet5);
    sheet5.classList.remove("run-animation");
    var stylec5 = document.createElement('style');
    stylec5.type = 'text/css';
    stylec5.id = 'stylec5';
    document.head.appendChild(stylec5);
    stylec5.sheet.insertRule(keys, stylec5.length);
  }
  addAnimationC5(`
    @keyframes barometize5 {
      0% { position: absolute; height: 50px; border-radius: 1%; transform: translate(440%, 0%); height: `+ oldh5 +`px; margin-top:` + oldm5 + `px; font-size: ` + C5Label + `px;}
      20% { height: 50px; transform: translate(440%, 0%); border-radius: 1%; font-size: 0; margin-top: 0px;}
      30% { height: 50px; transform: translate(440%, 0%); border-radius: 100%; font-size: 0 }
      50% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      60% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      65% { height: 50px; transform: translate(440%, 0%); border-radius: 100%; }
      70% { height: 50px; transform: translate(440%, 0%); border-radius: 10%; margin-top: 0px; }
      85% { transform: translate(440%, 0%); height: `+ c5h +`px; margin-top: ` + c5m + `px;  font-size: 0px;}
      100% { transform: translate(440%, 0%); height: `+ c5h +`px; margin-top:` + c5m + `px; border-radius: 1%; font-size: ` + C5Label + `px; }
    }
  `);

  function addAnimationAxis(keys) {
    var styleAxis = document.createElement('style');
    styleAxis.type = 'text/css';
    document.head.appendChild(styleAxis);
    styleAxis.sheet.insertRule(keys, styleAxis.length);
  }
  addAnimationAxis(`
    @keyframes axisize {
      0% { height: 50px; width: 50px; transform: translate(175%,-190%); }
      20% { height: 50px; width: 50px; transform: translate(-4%, -6%); border-radius: 100%; border-color: white; }
      25% { height: 50px; width:50px; transform: translate(-4%, -6%); border-radius: 100%; border-color: transparent; transition: border-color .5s ease; background: transparent; }
      40% { height: 50px; width:50px; transform: translate(-4%, -6%); border-radius: 30%; border-color: transparent; background: transparent;  }
      60% { height: 0px; width: 285px; background: white; transform: translate(-3%, -10%); border-color: transparent; border-radius: 0;}
      100% { height: 0px; width: 285px; background: white; left: 20px; transform: translate(0%, 0%); border-color: transparent; border-radius: 0; }
    }
  `);

  objc1.style['animation-name'] = 'barometize';
  objc2.style['animation-name'] = 'barometize2';
  objc3.style['animation-name'] = 'barometize3';
  objc4.style['animation-name'] = 'barometize4';
  objc5.style['animation-name'] = 'barometize5';
  axis.style['animation-name'] = 'axisize';

};

function update_labs(evnt){
  var lab1 = document.querySelector('.lab1');
  var lab2 = document.querySelector('.lab2');
  var lab3 = document.querySelector('.lab3');
  var lab4 = document.querySelector('.lab4');
  var lab5 = document.querySelector('.lab5');
  // Call the first batch of updates
  lab1.style.transition = "none";
  lab1.style['opacity'] = 0;
  // Force the browser recalculate the styles
  lab1.offsetHeight;
  lab1.style.transition = null;
  lab1.style['opacity'] = 1;
  lab1.style['transition'] = 'opacity 2s linear';
  lab1.style['transition-delay'] = '4s';
  // Call the first batch of updates
  lab2.style.transition = "none";
  lab2.style['opacity'] = 0;
  // Force the browser recalculate the styles
  lab2.offsetHeight;
  lab2.style.transition = null;
  lab2.style['opacity'] = 1;
  lab2.style['transition'] = 'opacity 2s linear';
  lab2.style['transition-delay'] = '4s';
  // Call the first batch of updates
  lab3.style.transition = "none";
  lab3.style['opacity'] = 0;
  // Force the browser recalculate the styles
  lab3.offsetHeight;
  lab3.style.transition = null;
  lab3.style['opacity'] = 1;
  lab3.style['transition'] = 'opacity 2s linear';
  lab3.style['transition-delay'] = '4s';
  // Call the first batch of updates
  lab4.style.transition = "none";
  lab4.style['opacity'] = 0;
  // Force the browser recalculate the styles
  lab4.offsetHeight;
  lab4.style.transition = null;
  lab4.style['opacity'] = 1;
  lab4.style['transition'] = 'opacity 2s linear';
  lab4.style['transition-delay'] = '4s';
  // Call the first batch of updates
  lab5.style.transition = "none";
  lab5.style['opacity'] = 0;
  // Force the browser recalculate the styles
  lab5.offsetHeight;
  lab5.style.transition = null;
  lab5.style['opacity'] = 1;
  lab5.style['transition'] = 'opacity 2s linear';
  lab5.style['transition-delay'] = '4s';

};

setTimeout(function(){

  var c1 = document.getElementById('circle1').innerHTML;
  var c2 = document.getElementById('circle2').innerHTML;
  var c3 = document.getElementById('circle3').innerHTML;
  var c4 = document.getElementById('circle4').innerHTML;
  var c5 = document.getElementById('circle5').innerHTML;

  var maxC = Math.max(c1,c2,c3,c4,c5);

  function barHeight(bar) {
    return (((bar / maxC) * 100 ) * 2);
  }

  function marTop(barH) {
    return ((barH-2)*-1)
  }

  var c1h = barHeight(c1)
  var c2h = barHeight(c2)
  var c3h = barHeight(c3)
  var c4h = barHeight(c4)
  var c5h = barHeight(c5)
  var c1m = marTop(c1h)
  var c2m = marTop(c2h)
  var c3m = marTop(c3h)
  var c4m = marTop(c4h)
  var c5m = marTop(c5h)

  if (c1h > 17) {
    var C1Label = 16
  } else {
    var C1Label = 0
  };
  if (c2h > 17) {
    var C2Label = 16
  } else {
    var C2Label = 0
  };
  if (c3h > 17) {
    var C3Label = 16
  } else {
    var C3Label = 0
  };
  if (c4h > 17) {
    var C4Label = 16
  } else {
    var C4Label = 0
  };
  if (c5h > 17) {
    var C5Label = 16
  } else {
    var C5Label = 0
  };

  var objc1 = document.querySelector('.circle1');
  var objc2 = document.querySelector('.circle2');
  var objc3 = document.querySelector('.circle3');
  var objc4 = document.querySelector('.circle4');
  var objc5 = document.querySelector('.circle5');
  var axis = document.getElementById('axis1')

  function addAnimationC1(keys) {
    var stylec1 = document.createElement('style');
    stylec1.type = 'text/css';
    stylec1.id = 'stylec1';
    document.head.appendChild(stylec1);
    stylec1.sheet.insertRule(keys, stylec1.length);
  }
  addAnimationC1(`
    @keyframes barometize {
      0% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      30% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      40% { height: 50px; transform: translate(0%, 0%); border-radius: 10%; margin-top: 0px; }
      70% { height: `+ c1h +`px; margin-top: ` + c1m + `px; font-size: 0px; }
      100% { position: absolute; height: `+ c1h +`px; margin-top:` + c1m + `px; border-radius: 1%; font-size: ` + C1Label + `px; }
    }
  `);

  function addAnimationC2(keys) {
    var stylec2 = document.createElement('style');
    stylec2.type = 'text/css';
    stylec2.id = 'stylec2';
    document.head.appendChild(stylec2);
    stylec2.sheet.insertRule(keys, stylec2.length);
  }
  addAnimationC2(`
    @keyframes barometize2 {
      0% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      30% { height: 50px; transform: translate(110%, 0%); border-radius: 100%; }
      40% { height: 50px; transform: translate(110%, 0%); border-radius: 10%; margin-top: 0px; }
      65% { transform: translate(110%, 0%); height: `+ c2h +`px; margin-top: ` + c2m + `px; font-size: 0px; }
      100% { transform: translate(110%, 0%); height: `+ c2h +`px; margin-top:` + c2m + `px; border-radius: 1%; font-size: ` + C2Label + `px; }
    }
  `);

  function addAnimationC3(keys) {
    var stylec3 = document.createElement('style');
    stylec3.type = 'text/css';
    stylec3.id = 'stylec3';
    document.head.appendChild(stylec3);
    stylec3.sheet.insertRule(keys, stylec3.length);
  }
  addAnimationC3(`
    @keyframes barometize3 {
      0% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      30% { height: 50px; transform: translate(220%, 0%); border-radius: 100%; }
      40% { height: 50px; transform: translate(220%, 0%); border-radius: 10%; margin-top: 0px; }
      60% { transform: translate(220%, 0%); height: `+ c3h +`px; margin-top: ` + c3m + `px;  font-size: 0px;}
      100% { transform: translate(220%, 0%); height: `+ c3h +`px; margin-top:` + c3m + `px; border-radius: 1%; font-size: ` + C3Label + `px; }
    }
  `);

  function addAnimationC4(keys) {
    var stylec4 = document.createElement('style');
    stylec4.type = 'text/css';
    stylec4.id = 'stylec4';
    document.head.appendChild(stylec4);
    stylec4.sheet.insertRule(keys, stylec4.length);
  }
  addAnimationC4(`
    @keyframes barometize4 {
      0% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      30% { height: 50px; transform: translate(330%, 0%); border-radius: 100%; }
      40% { height: 50px; transform: translate(330%, 0%); border-radius: 10%; margin-top: 0px; }
      65% { transform: translate(330%, 0%); height: `+ c4h +`px; margin-top: ` + c4m + `px; font-size: 0px; }
      100% { transform: translate(330%, 0%); height: `+ c4h +`px; margin-top:` + c4m + `px; border-radius: 1%;  font-size: ` + C4Label + `px;}
    }
  `);

  function addAnimationC5(keys) {
    var stylec5 = document.createElement('style');
    stylec5.type = 'text/css';
    stylec5.id = 'stylec5';
    document.head.appendChild(stylec5);
    stylec5.sheet.insertRule(keys, stylec5.length);
  }
  addAnimationC5(`
    @keyframes barometize5 {
      0% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      30% { height: 50px; transform: translate(440%, 0%); border-radius: 100%; }
      40% { height: 50px; transform: translate(440%, 0%); border-radius: 10%; margin-top: 0px; }
      70% { transform: translate(440%, 0%); height: `+ c5h +`px; margin-top: ` + c5m + `px;  font-size: 0px;}
      100% { transform: translate(440%, 0%); height: `+ c5h +`px; margin-top:` + c5m + `px; border-radius: 1%; font-size: ` + C5Label + `px; }
    }
  `);

  function addAnimationAxis(keys) {
    var styleAxis = document.createElement('style');
    styleAxis.type = 'text/css';
    styleAxis.id = 'styleAxis';
    document.head.appendChild(styleAxis);
    styleAxis.sheet.insertRule(keys, styleAxis.length);
  }
  addAnimationAxis(`
    @keyframes axisize {
      0% { height: 50px; width: 50px; transform: translate(175%,-190%); }
      20% { height: 50px; width: 50px; transform: translate(-4%, -6%); border-radius: 100%; border-color: white; }
      25% { height: 50px; width:50px; transform: translate(-4%, -6%); border-radius: 100%; border-color: transparent; transition: border-color .5s ease; background: transparent; }
      40% { height: 50px; width:50px; transform: translate(-4%, -6%); border-radius: 30%; border-color: transparent; background: transparent;  }
      60% { height: 0px; width: 285px; background: white; transform: translate(-3%, -10%); border-color: transparent; border-radius: 0;}
      100% { height: 0px; width: 285px; background: white; left: 20px; transform: translate(0%, 0%); border-color: transparent; border-radius: 0; }
    }
  `);

  var lab1 = document.querySelector('.lab1');
  var lab2 = document.querySelector('.lab2');
  var lab3 = document.querySelector('.lab3');
  var lab4 = document.querySelector('.lab4');
  var lab5 = document.querySelector('.lab5');
  var barTitle = document.getElementById('.barTitle')

  lab1.style['opacity'] = 1;
  lab1.style['transition'] = 'opacity 2s linear';
  lab1.style['transition-delay'] = '4s';

  lab2.style['opacity'] = 1;
  lab2.style['transition'] = 'opacity 2s linear';
  lab2.style['transition-delay'] = '4s';

  lab3.style['opacity'] = 1;
  lab3.style['transition'] = 'opacity 2s linear';
  lab3.style['transition-delay'] = '4s';

  lab4.style['opacity'] = 1;
  lab4.style['transition'] = 'opacity 2s linear';
  lab4.style['transition-delay'] = '4s';

  lab5.style['opacity'] = 1;
  lab5.style['transition'] = 'opacity 2s linear';
  lab5.style['transition-delay'] = '4s';

  objc1.style['animation-name'] = 'barometize';
  objc2.style['animation-name'] = 'barometize2';
  objc3.style['animation-name'] = 'barometize3';
  objc4.style['animation-name'] = 'barometize4';
  objc5.style['animation-name'] = 'barometize5';
  axis.style['animation-name'] = 'axisize';

  const dateChange = document.getElementById("circle1");
  const dateChange2 = document.getElementById("circle2");
  const dateChange3 = document.getElementById("circle3");
  const dateChange4 = document.getElementById("circle4");
  const dateChange5 = document.getElementById("circle5");

  dateChange.addEventListener("DOMCharacterDataModified", function (evt) {
      update_bars(evt);
      update_labs(evt);
  }, false);
  dateChange2.addEventListener("DOMCharacterDataModified", function (evt) {
      update_bars(evt);
      update_labs(evt);
  }, false);
  dateChange3.addEventListener("DOMCharacterDataModified", function (evt) {
      update_bars(evt);
      update_labs(evt);
  }, false);
  dateChange4.addEventListener("DOMCharacterDataModified", function (evt) {
      update_bars(evt);
      update_labs(evt);
  }, false);
  dateChange5.addEventListener("DOMCharacterDataModified", function (evt) {
      update_bars(evt);
      update_labs(evt);
  }, false);

  // lab1.addEventListener("DOMCharacterDataModified", function (evt) {
  //   // Call the first batch of updates
  //   lab1.style.transition = "none";
  //   lab1.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab1.offsetHeight;
  //   lab1.style.transition = null;
  //   lab1.style['opacity'] = 1;
  //   lab1.style['transition'] = 'opacity 2s linear';
  //   lab1.style['transition-delay'] = '4s';
  // }, false);
  //
  // lab2.addEventListener("DOMCharacterDataModified", function (evt) {
  //   // Call the first batch of updates
  //   lab2.style.transition = "none";
  //   lab2.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab2.offsetHeight;
  //   lab2.style.transition = null;
  //   lab2.style['opacity'] = 1;
  //   lab2.style['transition'] = 'opacity 2s linear';
  //   lab2.style['transition-delay'] = '4s';
  // }, false);
  //
  // lab3.addEventListener("DOMCharacterDataModified", function (evt) {
  //   // Call the first batch of updates
  //   lab2.style.transition = "none";
  //   lab2.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab2.offsetHeight;
  //   lab2.style.transition = null;
  //   lab2.style['opacity'] = 1;
  //   lab2.style['transition'] = 'opacity 2s linear';
  //   lab2.style['transition-delay'] = '4s';
  //   // Call the first batch of updates
  //   lab3.style.transition = "none";
  //   lab3.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab3.offsetHeight;
  //   lab3.style.transition = null;
  //   lab3.style['opacity'] = 1;
  //   lab3.style['transition'] = 'opacity 2s linear';
  //   lab3.style['transition-delay'] = '4s';
  //   // Call the first batch of updates
  //   lab4.style.transition = "none";
  //   lab4.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab4.offsetHeight;
  //   lab4.style.transition = null;
  //   lab4.style['opacity'] = 1;
  //   lab4.style['transition'] = 'opacity 2s linear';
  //   lab4.style['transition-delay'] = '4s';
  //   // Call the first batch of updates
  //   lab5.style.transition = "none";
  //   lab5.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab5.offsetHeight;
  //   lab5.style.transition = null;
  //   lab5.style['opacity'] = 1;
  //   lab5.style['transition'] = 'opacity 2s linear';
  //   lab5.style['transition-delay'] = '4s';
  // }, false);
  //
  // lab4.addEventListener("DOMCharacterDataModified", function (evt) {
  //   // Call the first batch of updates
  //   lab4.style.transition = "none";
  //   lab4.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab4.offsetHeight;
  //   lab4.style.transition = null;
  //   lab4.style['opacity'] = 1;
  //   lab4.style['transition'] = 'opacity 2s linear';
  //   lab4.style['transition-delay'] = '4s';
  // }, false);
  //
  // lab5.addEventListener("DOMCharacterDataModified", function (evt) {
  //   // Call the first batch of updates
  //   lab5.style.transition = "none";
  //   lab5.style['opacity'] = 0;
  //   // Force the browser recalculate the styles
  //   lab5.offsetHeight;
  //   lab5.style.transition = null;
  //   lab5.style['opacity'] = 1;
  //   lab5.style['transition'] = 'opacity 2s linear';
  //   lab5.style['transition-delay'] = '4s';
  // }, false);


}, 2000);
