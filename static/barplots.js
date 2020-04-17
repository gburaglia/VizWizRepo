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
    document.head.appendChild(stylec5);
    stylec5.sheet.insertRule(keys, stylec5.length);
  }
  addAnimationC5(`
    @keyframes barometize5 {
      0% { height: 50px; transform: translate(200%,-200%); border-radius: 100%; }
      20% { height: 50px; transform: translate(0%, 0%); border-radius: 100%; }
      30% { height: 50px; transform: translate(440%, 0%); border-radius: 100%; }
      40% { height: 50px; transform: translate(440%, 0%); border-radius: 10%; margin-top: 0px; }
      65% { transform: translate(440%, 0%); height: `+ c5h +`px; margin-top: ` + c5m + `px;  font-size: 0px;}
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

}, 3000);
