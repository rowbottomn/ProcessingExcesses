
//global variables
//position arrays
int maxSize = 300;
PVector[] tracers = new PVector[maxSize];
PVector[] vels = new PVector[maxSize];
PVector grav = new PVector(0,0.045);
float [] xs = new float[maxSize];
float [] ys = new float[maxSize];
float [] sizes = new float [maxSize];
float startSize = 60;//this is the tracers starting size
float shrinkScale = 0.99;

//setup function
void setup(){
   size(800,800); 
   noStroke();
   frameRate(120);
   
   init();
}

//custom functions
void init(){
   //initialize the arrays
   for (int i = 0; i < maxSize; i++){
       tracers[i] = new PVector(-1000, -1000);
       vels[i] = PVector.random2D();
       xs[i] = -1000;
       ys[i] = -1000;
       sizes[i] = startSize;
   }
   
}

//builtin functions



//draw function
void draw(){
  background(50);
  //update stuff
  //copy the positions to the elements on the right
  for(int i = maxSize - 1; i > 0; i--){
    tracers[i] = tracers[i-1];
    vels[i] = vels[i-1].add(grav);
    tracers[i].add(vels[i]);
     xs[i] = xs[i-1];
     ys[i] = ys[i-1];
     sizes[i] = sizes[i-1]*shrinkScale;
    // print(i);
  }
  
  //get a current position from the mouse and set 1st element
  xs[0] = mouseX;
  ys[0] = mouseY;
  tracers[0] = new PVector(mouseX, mouseY);
  sizes[0] = startSize;
  vels[0] = PVector.random2D(); 
  //check stuff
 
   //draw stuff
   
   for(int i = 0; i < maxSize; i++){
     //fill(50 + (float)i/maxSize*205, 128 + 127*sin((float)frameCount*PI/60), 128 + 127*cos((float)frameCount*PI/31), 255. - (float)i/maxSize*255.);
          fill(50 + (float)i/maxSize*205, 250 + 50*sin((float)frameCount*PI/60), 255, 255. - (float)i/maxSize*255.);

      ellipse(tracers[i].x, tracers[i].y, sizes[i],sizes[i]);  
   }
}
