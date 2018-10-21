/*-----------------------------------------------
     ductPsiOmega3DG1.js
     流れ関数-渦度法
     3Dグラフィックス     
------------------------------------------------*/
var canvas;//canvas要素
var gl;    //WebGL描画用コンテキスト
var camera;//カメラ
var light; //光源
var flagDebug = false;
//animation
var fps ; //フレームレート
var lastTime;
var elapseTime = 0.0;//全経過時間
var elapseTime0 = 0.0;
var elapseTime1 = 0.0;
var flagStart = false;
var flagStep = false;
var flagReset = false;
//表示オブジェクト
var object, obstacle;
var adjustH = 0.01;//表示上の高さ調整
var displayMode = 0;//渦度/流れ関数
var colorMode = 0;//連続／段階表示
//数値計算
var Psi = [];  //流れ関数
var Omg = [];//渦度
var gx = [];   //ｘ方向微分
var gy = [];   //ｙ方向微分
var VelX = []; //ｘ方向速度
var VelY = []; //ｙ方向速度
var type = [];//格子点のタイプ

var deltaT = 0.001;
var Re = 3000.0;//レイノルズ数

var maxPsi = 1.0;
var minPsi = 0;
var maxOmg = 20.0;
var minOmg = -20.0;

//解析領域矩形
function Rect()
{
  this.nMeshX = 160;//x方向割数
  this.nMeshY = 80; //y方向分割数
  this.size = new Vector3(2, 1, 0);//矩形ダクト領域のサイズ（固定）
  this.left0 = new Vector3(-1, -1, 0);//その左下位置
  this.delta = new Vector3(); //格子間隔
  this.obs_nX0 = 30;  //左端から障害物中心までの距離(格子間隔の整数倍）
  this.obs_nWX = 8;//障害物の厚さ(ｘ方向,格子間隔の整数倍)
  this.obs_nWY = 40; //障害物の幅(ｙ方向,格子間隔の整数倍)
  this.obs_left;//ダクト左端から障害物左端までの距離(仮の値）
}
var rect = new Rect();
var NX, NY, DX, DY;

function webMain() 
{
  //canvas要素を取得する
  canvas = document.getElementById('WebGL');
  // WebGL描画用のコンテキストを取得する
  gl = WebGLUtils.setupWebGL(canvas);
  if (!gl) 
  {
    alert('WebGLコンテキストの取得に失敗');
    return;
  }
  var VS_SOURCE = document.getElementById("vs").textContent;
  var FS_SOURCE = document.getElementById("fs").textContent;

  
  if(!initGlsl(gl, VS_SOURCE, FS_SOURCE))
  {
    alert("GLSLの初期化に失敗");
    return;
  }
  
  //canvasをクリアする色を設定する
  gl.clearColor(0.1, 0.1, 0.1, 1);
  gl.enable(gl.DEPTH_TEST);

  form1.deltaT.value = deltaT;
  form1.Re.value = Re;
  form1.nMeshX.value = rect.nMeshX;
  form1.nMeshY.value = rect.nMeshY;
  form1.obs_nX0.value = rect.obs_nX0;
  form1.obs_nWX.value = rect.obs_nWX;
  form1.obs_nWY.value = rect.obs_nWY;
  form2.adjustH.value = adjustH;
  form2.maxPsi.value = maxPsi;
  form2.minPsi.value = minPsi;
  form2.maxOmg.value = maxOmg;
  form2.minOmg.value = minOmg;
  
  initCamera();
  initData();
  display();
  
  var timestep = 0;
  var animate = function()
  {
    //繰り返し呼び出す関数を登録
    requestAnimationFrame(animate, canvas); //webgl-utilsで定義
    //時間計測
    var currentTime = new Date().getTime();
    var frameTime = (currentTime - lastTime) / 1000.0;//時間刻み[sec]
    elapseTime1 += frameTime;
    fps ++;
    if(elapseTime1 >= 0.5)
    {
      form1.fps.value = 2*fps.toString(); //1秒間隔で表示
      timestep = 1 / (2*fps);
      form1.step.value = timestep.toString();
      fps = 0;
      elapseTime1 = 0.0;
    }
    lastTime = currentTime;　
    if(flagStart)
    { 
      elapseTime += frameTime;
      elapseTimeN += deltaT;//数値計算上の経過時間（無次元時間）
        
      //for(var i = 0; i < 10; i++)
      calculate(); 
      display();
      
      elapseTime0 = elapseTime;//現在の経過時間を保存
      elapseTimeN0 = elapseTimeN;//現在の経過時間を保存
      
      form1.e_time.value = elapseTime.toString();
      form1.n_time.value = elapseTimeN.toString();
      
      if(flagStep) { flagStart = false; } 
    }      
  }
  animate();

}

//--------------------------------------------
function initCamera()
{
　//光源インスタンスを作成
  light = new Light();
  light.pos = [50.0, -100.0, 100.0, 1.0];
  form2.lightX.value = light.pos[0];
  form2.lightY.value = light.pos[1];
  form2.lightZ.value = light.pos[2];
    
　//カメラ・インスタンスを作成
  camera = new Camera();
  camera.phi = -90; 
  camera.cnt[2] = 0.2;
  camera.dist = 4;
  camera.fovy = 15;
  camera.getPos();//カメラ位置を計算
  mouseOperation(canvas, camera);//swgSupport.js
}

function initData()
{
  deltaT = parseFloat(form1.deltaT.value);
  Re = parseFloat(form1.Re.value);
  NX = parseInt(form1.nMeshX.value);
  NY = parseInt(form1.nMeshY.value);

  rect.obs_nX0 = parseFloat(form1.obs_nX0.value);
  rect.obs_nWX = parseFloat(form1.obs_nWX.value);
  rect.obs_nWY = parseFloat(form1.obs_nWY.value);

  DX = rect.size.x / NX;//格子間隔
  DY = rect.size.y / NY;
  var nMeshX0 = rect.obs_nX0;
  var nMeshX1 = nMeshX0 - rect.obs_nWX/2;
  var nMeshX2 = nMeshX1 + rect.obs_nWX;
  var nObsWX = rect.obs_nWX;
  var nObsWY = rect.obs_nWY;
  rect.obs_left = nMeshX1 * DX;//ダクト左端からの距離

  var i, j;
  
  for(i = 0; i <= NX; i++)
  {
    type[i] = [];//格子点のタイプ
    Psi[i] = [];  //流れ関数
    Omg[i] = [];//渦度
    gx[i] = [];   //ｘ方向微分
    gy[i] = [];   //ｙ方向微分
    VelX[i] = []; //ｘ方向速度
    VelY[i] = []; //ｙ方向速度
  }  

  //格子点のタイプ
  for(j = 0; j <= NY; j++)
  {
	for(i = 0; i <= NX; i++)
    {
	  type[i][j] = "INSIDE";//内点
	  if(j == 0) type[i][j] = "BOTTOM";//下側壁面
	  if(j == NY) type[i][j] = "TOP";//上側壁面
	  if(i == 0) type[i][j] = "INLET";//流入端
	  if(i == NX) type[i][j] = "OUTLET";//流出端
	  if(i == nMeshX1 && j < nObsWY) type[i][j] = "OBS_LEFT";//障害物左端
	  if(i >= nMeshX1 && i <= nMeshX2 && j == nObsWY) type[i][j] = "OBS_TOP";//障害物上端
	  if(i == nMeshX2 && j < nObsWY) type[i][j] = "OBS_RIGHT";//障害物右端
	  if(i > nMeshX1 && i < nMeshX2 && j < nObsWY) type[i][j] = "OBSTACLE";//障害物内部
	  //障害物のコーナー
	  if(i == nMeshX1 && j == 0) type[i][j] = "OBS_UL";
	  if(i == nMeshX1 && j == nObsWY)  type[i][j] = "OBS_UL";
	  if(i == nMeshX2 && j == 0) type[i][j] = "OBS_UR";
	  if(i == nMeshX2 && j == nObsWY) type[i][j] = "OBS_UR";
	}
  }

  //初期値
  //入口/出口は流速1,psi = y
  //下の壁は psi = 0，上の壁は psi = rect.size.y
  for(j = 0; j <= NY; j++)
	for (i = 0; i <= NX; i++)
	{
	  //流れ関数
	  if(type[i][j] == "TOP") Psi[i][j] = rect.size.y;
	  else if(type[i][j] == "INLET" || type[i][j] == "OUTLET" || type[i][j] == "INSIDE" ) Psi[i][j] = j * DY;
      else Psi[i][j] = 0.0;
	  //渦度
	  Omg[i][j] = 0.0;
      //速度
	  if(type[i][j] == "INLET" || type[i][j] == "OUTLET" || type[i][j] == "INSIDE") VelX[i][j] = 1.0;
	  else VelX[i][j] = 0.0;
      VelY[i][j] = 0.0;
      //CIP法で使用する微分値
      gx[i][j] = 0.0;
      gy[i][j] = 0.0;
    }

  calcVelocity();

  maxPsi0 = -1000.0; minPsi0 = 1000.0;
  maxOmg0 = -1000.0; minOmg0 = 1000.0;

  //発散しないための目安を知るため
  var courant, diffNum;
  if(DX < DY)
  {
    courant = 1.0 * deltaT / DX;	
	diffNum = (1.0 / Re) * deltaT / (DX * DX);//拡散数
  }
  else
  {
 	courant = 1.0 * deltaT / DY;	
	diffNum = (1.0 / Re) * deltaT / (DX * DY);//拡散数
  }
  form1.courant.value = courant;
  form1.diffNum.value = diffNum;


  initObject();
}

function initObject()
{
  //解析結果表示オブジェクト
  object = new Rigid();//Rigidクラスのオブジェクトを表示オブジェクト
  object.kind  = "ELEVATION";
  object.sizeX = rect.size.x;
  object.sizeY = rect.size.y;
  object.vSize = new Vector3(1, 1, adjustH);//scaling  
  object.nSlice = NX;
  object.nStack = NY;
  object.diffuse = [ 0.4, 0.6, 0.9, 1.0] ;
  object.ambient = [ 0.1, 0.2, 0.3, 1.0];
  object.specular = [ 0.8, 0.8, 0.8, 1.0];
  object.shininess = 100.0;
  object.flagDebug = flagDebug;
  //障害物
  obstacle = new Rigid();
  obstacle.kind = "CUBE";
  obstacle.vSize = new Vector3(rect.obs_nWX*DX, rect.obs_nWY*DY, 0.1);
  obstacle.vPos = new Vector3(rect.obs_nX0*DX - rect.size.x/2, (rect.obs_nWY*DY - rect.size.y)/2, 0);
  obstacle.flagDebug = flagDebug;
  
}

function display()
{
  //光源
  var lightPosLoc = gl.getUniformLocation(gl.program, 'u_lightPos');
  gl.uniform4fv(lightPosLoc, light.pos);
  var lightColLoc = gl.getUniformLocation(gl.program, 'u_lightColor');
  gl.uniform4fv(lightColLoc, light.color);
  
  var cameraLoc = gl.getUniformLocation(gl.program, 'u_cameraPos');
  gl.uniform3fv(cameraLoc, camera.pos);
  
  //ビュー投影行列を計算する
  var vpMatrix = new Matrix4();// 初期化
  vpMatrix.perspective(camera.fovy, canvas.width/canvas.height, camera.near, camera.far);
  if(Math.cos(Math.PI * camera.theta /180.0) >= 0.0)//カメラ仰角90度でﾋﾞｭｰｱｯﾌﾟﾍﾞｸﾄﾙ切替
	  vpMatrix.lookAt(camera.pos[0], camera.pos[1], camera.pos[2], camera.cnt[0], camera.cnt[1], camera.cnt[2], 0.0, 0.0, 1.0);
  else
	  vpMatrix.lookAt(camera.pos[0], camera.pos[1], camera.pos[2], camera.cnt[0], camera.cnt[1], camera.cnt[2], 0.0, 0.0, -1.0);

  var vpMatrixLoc = gl.getUniformLocation(gl.program, 'u_vpMatrix');
  gl.uniformMatrix4fv(vpMatrixLoc, false, vpMatrix.elements);

  var colorLoc = gl.getUniformLocation(gl.program, 'u_colorMode');
  gl.uniform1i(colorLoc, colorMode);

  // カラーバッファとデプスバッファをクリアする
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  gl.viewport(0, 0, canvas.width, canvas.height);

  var i, j, k;
  var range0;
  maxPsi = parseFloat(form2.maxPsi.value);
  minPsi = parseFloat(form2.minPsi.value);
  maxOmg = parseFloat(form2.maxOmg.value);
  minOmg = parseFloat(form2.minOmg.value);

  for(j = 0; j <= NY; j++)
    for(i = 0; i <= NX; i++)
    {
      k = i + j * (NX+ 1);
      
      if( displayMode == 0 ) 
      {
        range0 = maxOmg - minOmg;
        object.data[k] = (Omg[i][j] - minOmg) / range0 ;
      }
      else  
      {
        range0 = maxPsi - minPsi;
        object.data[k] = (Psi[i][j] - minPsi) / range0 ;
      }

    }

  object.vSize = new Vector3(1, 1, adjustH);  
  object.vPos.z = -adjustH * 0.5;//中間色(G)をz=0の位置にする
  var n = object.initVertexBuffers(gl);
  object.draw(gl, n);

  //障害物
  gl.uniform1i(colorLoc, 2);
  n = obstacle.initVertexBuffers(gl);
  obstacle.draw(gl, n);

}

function calculate()
{
  var i, j;
  var iteration = 10;//最大繰り返し回数(Poisson方程式）
  var tolerance = 0.00001;//許容誤差
  var error = 0.0;
  var maxError = 0.0;
  var pp;
  var DX2 = DX * DX;
  var DY2 = DY * DY;
  var DD2 = DX2 + DY2;//corner

  //渦度境界条件
  for (i = 0; i <= NX; i++)
	for (j = 0; j <= NY; j++) 
	{
	  if(type[i][j] == "INSIDE") continue;
	  else if(type[i][j] == "INLET") Omg[i][j] = 0.0;//Dirichlet
	  else if(type[i][j] == "OUTLET") Omg[i][j] = Omg[i-1][j];//Neumann
	  else if(type[i][j] == "TOP") Omg[i][j] = -2.0 *( Psi[i][NY-1] - rect.size.y) / DY2;
	  else if(type[i][j] == "BOTTOM") Omg[i][j] = -2.0 * Psi[i][1] / DY2;
	  else if(type[i][j] == "OBS_LEFT") Omg[i][j] = -2.0 * Psi[i-1][j] / DX2;
	  else if(type[i][j] == "OBS_TOP") Omg[i][j] = -2.0 * Psi[i][j+1] / DY2;
	  else if(type[i][j] == "OBS_RIGHT") Omg[i][j] = -2.0 * Psi[i+1][j] / DX2;
	  else if(type[i][j] == "OBS_UL") Omg[i][j] = -2.0 * Psi[i-1][j+1] / DD2;
	  else if(type[i][j] == "OBS_UR") Omg[i][j] = -2.0 * Psi[i+1][j+1] / DD2;
    }

  //Poissonの方程式を解く
  var cnt = 0;
  while (cnt < iteration)
  {
    maxError = 0.0;
	for (i = 1; i < NX; i++)
	  for (j = 1; j < NY; j++)
	  {
	    if(type[i][j] != "INSIDE") continue;
		pp = ( DY2 * (Psi[i-1][j] + Psi[i+1][j]) + DX2 *(Psi[i][j-1] + Psi[i][j+1])
	       + Omg[i][j] * DX2 * DY2 ) / (2.0 * (DX2 + DY2));
	    error = Math.abs(pp - Psi[i][j]);
		if (error > maxError) maxError = error;
	    Psi[i][j] = pp;//更新
	  }
	  
    if (maxError < tolerance) break;
	cnt++;
  }
//console.log("cnt = " + cnt + " maxEr = " + maxError + " Psi = " + Psi[10][10] + " Omg = " + Omg[10][10]);
  calcVelocity();//速度の更新(ψ→ω変換)

  //渦度輸送方程式を解く

  methodCIP();

  //流れ関数，渦度の最小値，最大値
  for(i = 1; i < NX; i++)
	for (j = 1; j < NY; j++)
	{
      if(type[i][j] >= "OBS_LEFT")  continue;
	  if(Psi[i][j] > maxPsi0) maxPsi0 = Psi[i][j];
	  if(Psi[i][j] < minPsi0) minPsi0 = Psi[i][j];
	  if(Omg[i][j] > maxOmg0) maxOmg0 = Omg[i][j];
	  if(Omg[i][j] < minOmg0) minOmg0 = Omg[i][j];
	}
console.log("maxPsi= " + maxPsi0 + " minPsi = " + minPsi0);
console.log("maxOmg= " + maxOmg0 + " minOmg = " + minOmg0);

}

function calcVelocity()
{
  //速度ベクトルの計算
  //格子点の速度ベクトル(上下左右の流れ関数の差で求める)
  var i, j;
 
  for (j = 1; j < NY; j++)
	for(i = 1; i < NX; i++)
	{
      if(type[i][j] != "INSIDE") continue;
	  //ポテンシャルの低い方から高い方へ
	  VelX[i][j] = (Psi[i][j+1] - Psi[i][j-1]) / (DY * 2.0);
	  VelY[i][j] = (Psi[i-1][j] - Psi[i+1][j]) / (DX * 2.0);
// if(j == 20) console.log("i = " + i + " v.x = " + VelX[i][j] + " v.y = " + VelY[i][j]);
	}
}

function methodCIP()
{
  var newOmg = [];//新渦度
  var newGx = [];//x方向微分
  var newGy = [];//y方向微分
  var c11, c12, c21, c02, c30, c20, c03, a, b, sx, sy, x, y, dx, dx2, dx3, dy, dy2, dy3; 
	
  var i, j, ip, jp;
  for(i = 0; i <= NX; i++)
  {
    newOmg[i] = [];
    newGx[i] = [];
    newGy[i] = [];
  }


  for(j = 1; j < NY; j++)
	for(i = 1; i < NX; i++)
	{
      if(type[i][j] != "INSIDE") continue;

      if(VelX[i][j] >= 0.0) sx = 1.0; else sx = -1.0;
      if(VelY[i][j] >= 0.0) sy = 1.0; else sy = -1.0;

      x = - VelX[i][j] * deltaT;
	  y = - VelY[i][j] * deltaT;
	  ip = i - sx;//上流点
      jp = j - sy;
	  dx = sx * DX;
	  dy = sy * DY;
	  dx2 = dx * dx;
	  dx3 = dx2 * dx;
	  dy2 = dy * dy;
	  dy3 = dy2 * dy;

      c30 = ((gx[ip][j] + gx[i][j]) * dx - 2.0 * (Omg[i][j] - Omg[ip][j])) / dx3;
	  c20 = (3.0 * (Omg[ip][j] - Omg[i][j]) + (gx[ip][j] + 2.0 * gx[i][j]) * dx) / dx2;
	  c03 = ((gy[i][jp] + gy[i][j]) * dy - 2.0 * (Omg[i][j] - Omg[i][jp])) / dy3;
	  c02 = (3.0 * (Omg[i][jp] - Omg[i][j]) + (gy[i][jp] + 2.0 * gy[i][j]) * dy) / dy2;
      a = Omg[i][j] - Omg[i][jp] - Omg[ip][j] + Omg[ip][jp];
	  b = gy[ip][j] - gy[i][j];
	  c12 = (-a - b * dy) / (dx * dy2);
	  c21 = (-a - (gx[i][jp] - gx[i][j]) * dx) / (dx2*dy);
	  c11 = - b / dx + c21 * dx;

	  newOmg[i][j] = Omg[i][j] + ((c30 * x + c21 * y + c20) * x + c11 * y + gx[i][j]) * x
			        + ((c03 * y + c12 * x + c02) * y + gy[i][j]) * y;

	  newGx[i][j] = gx[i][j] + (3.0 * c30 * x + 2.0 * (c21 * y + c20)) * x + (c12 * y + c11) * y;
			newGy[i][j] = gy[i][j] + (3.0 * c03 * y + 2.0 * (c12 * x + c02)) * y + (c21 * x + c11) * x;

	  //粘性項に中央差分
	  newOmg[i][j] += deltaT * ( (Omg[i-1][j] - 2.0 * Omg[i][j] + Omg[i+1][j]) / dx2
							 + (Omg[i][j-1] - 2.0 * Omg[i][j] + Omg[i][j+1]) / dy2 ) / Re;

	}
  //更新
  for(j = 1; j < NY; j++)
	for(i = 1; i < NX; i++)
	{
      if(type[i][j] != "INSIDE") continue;
	  Omg[i][j] = newOmg[i][j];
	  gx[i][j] = newGx[i][j];
	  gy[i][j] = newGy[i][j];
	}			
}

//---------------------------------------------------
//イベント処理
function onClickC_Size()
{
  canvas.width = form1.c_sizeX.value;
  canvas.height = form1.c_sizeY.value;
  display();
}

function onChangeData()
{
  onClickReset();
  initData();
}

function onDisplay()
{
  display();
}

function onChangeAdjustH()
{
  adjustH = parseFloat(form2.adjustH.value);
  if(adjustH == 0) adjustH = 0.001;//　完全に0にするとmatrix4の逆行列ルーチンでエラーになる
  display();
}

function onChangeDisplayMode()
{
  var nn;
  var radioD = document.getElementsByName("radioD");
  for(var i = 0; i < radioD.length; i++)
  {
     if(radioD[i].checked) displayMode = i;
  }
  display();
}

function onChangeColorMode()
{
  var nn;
  var radioC = document.getElementsByName("radioC");
  for(var i = 0; i < radioC.length; i++)
  {
     if(radioC[i].checked) colorMode = i;
  }
  display();
}

function onClickDebug()
{
  object.flagDebug = obstacle.flagDebug = flagDebug = !flagDebug ;
  display(); 
}

function onClickStart()
{
  fps = 0;
  elapseTime = 0;
  elapseTime0 = 0;
  elapseTime1 = 0;
  elapseTimeN = 0;
  elapseTimeN0 = 0;
  flagStart = true;
  flagStep = false;
  flagFreeze = false;
  lastTime = new Date().getTime();
}
function onClickFreeze()
{
  flagStart = !flagStart;
  flagFreeze = !flagFreeze;
  
  flagStep = false;
}
function onClickStep()
{
  flagStep = true;
  flagStart = true;
  elapseTime = elapseTime0;
}
function onClickReset()
{
  elapseTime0 = 0;
  elapseTimeN0 = 0;
  flagStart = false;
  flagStep = false;
  initData();
  form1.e_time.value = "0";
  form1.n_time.value = "0";
  display();
}

function onClickCameraReset()
{
  initCamera();
  display();
}

function onClickCameraAbove()
{
  initCamera();
  camera.theta = 90.01;
  camera.getPos();//カメラ位置を計算
  display();
}

function onClickLight()
{
  light.pos[0] = parseFloat(form2.lightX.value);
  light.pos[1] = parseFloat(form2.lightY.value);
  light.pos[2] = parseFloat(form2.lightZ.value);
  display();
}



