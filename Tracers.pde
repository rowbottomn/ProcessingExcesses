//ArrayList <PVector> places = new ArrayList<PVector>();
int maxL = 50;
float [] xs = new float[maxL];
float [] ys = new float[maxL];
float [] sizs = new float[maxL];
float [] als = new float [maxL];

float startSize = 60.;

void setup(){
   size(600,600); 
    noStroke();  
}

void draw(){
  background(50);
  //move all the entries down a location
  for (int i = xs.length-1; i > 0; i--){
     xs[i] = xs[i-1]+1;
     ys[i] = ys[i-1];
     sizs[i] = sizs[i-1] - startSize/float(maxL);
     als[i] = als[i-1] - 0.01;
  }
  
  //add the current location to the start
  xs[0] = mouseX;
  ys[0] = mouseY;
  sizs[0] = startSize;
  als[0] = 255;
  
  for(int i = 0; i < xs.length; i++){
    fill(255, 255, 200, 255. - 255. * float(i) / float(maxL));
    ellipse(xs[i], ys[i], sizs[i], sizs[i]);
  }
}
