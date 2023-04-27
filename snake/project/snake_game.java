package classe.project;

import java.awt.Color;
import java.applet.*;
import java.awt.Font;
import java.awt.Image;
import java.awt.Toolkit;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

import hsa_ufa.Console;

public class snake_game { 
	static int interfaceOn;
	static final Color lightGreen=new Color(167, 217, 72); 
	static final Color darkGreen=new Color(142,204,57); 
	static int sleepTime=40;
	
	public static void main(String[] args) throws InterruptedException, UnsupportedAudioFileException, IOException, LineUnavailableException {
		Console c=new Console(900,600,20,"Snake");
		main_menu mm=new main_menu(c);
		game_interface gi=new game_interface(c);
		end_menu em=new end_menu(c);
		option opt=new option(c);
		
		/*- the main loop structure for the game itself 
		 	the switch statement are included to determine
		 	the interface that are using
		*/
		while (true){
			
			switch (interfaceOn) {
			
			case 0:
				mm.update();
				break;
			case 1:
				gi.update();
				break;
			case 2:
				opt.update();
				break;
			case 3:
				em.update();
				break;
			
			}
			
			Thread.sleep(sleepTime);
		}
	}
}


/*-
The interfaces class are the parent class of all graphic
related class. Method with in the class are likely going to be 
overridden in other class or being used in other class
 */
class interfaces{
	Console c;
	static int size=25;
	public final int Max_Width=900;
	public final int Max_Height=600;
	private button[] buttons;
	
	/*- 
	 constructor
	 
	 precondition: 
	 	consleUsing as a Console object 
	 postcondition:
		an interfaces object created 
	 */
	public interfaces(Console consleUsing) {
		c=consleUsing;
	}
	
	/*-
	This method will setup an array of button object.
	arrs is a 2d array and which array must have 5 element.
	each element represent the x, y, width, height and Purpose(
	-999 exit, 0 option, other numbers are interface jumping).
	texts are a array of String that represents the text you 
	want to have on each button.
	isSelected is for the current status of the button, the first button 
	will always be selected since the default position a selecter is at the first 
	button 
	
	precondition:
		arrs as 2d int array, texts as string array and isSelected as boolean array
		all arrays have the same length and each array in arrs have 5 element 
	postcondition:
		buttons array are created and initialized to size of the length of arrays
	 */
	public void setUpButtons(int[][] arrs,String[] texts, boolean[] isSelected) {
		buttons=new button[arrs.length];
		for (int i = 0; i < arrs.length; i++) {
			buttons[i]=new button(arrs[i][0],arrs[i][1],arrs[i][2],arrs[i][3],texts[i],isSelected[i],arrs[i][4],c);
		}

	}
	
	/*-
	 this display method will display all buttons,
	 it is being overridden in other class.
	 */
	public void display() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException {
		for (int i = 0; i < buttons.length; i++) {
			buttons[i].displayButton();
		}
	}
	
	/*-
	 This changeButtonStatus is here because a subclass can't access
	 the buttons array so this method(mutator method) allows a subclass
	 to change the status of specific button object 
	 
	 precondition:
	 	boolean which(which type of change),int button1(first button you want to change)
	 	and int button2(second button you want to change)
	 postcondition:
	 	the status are changed accordingly
	 */
	public void changeButtonStatus(boolean which,int button1,int button2){
		if (which) {
			buttons[button1].changeButtonStatus(true);
			buttons[button2].changeButtonStatus(true);
		} else {
			buttons[button2].changeButtonStatus(false);
		}
	}

	/*- 
	 change the interface that it's on currently to the interface
	 that it is suppose to be on
	 
	 precondition:
	 	int buttomNum (the button being clicked) 
	 postcondition:
	 	does the purpose of the button i.e. exit, change option or jump to
	 	next interface
	 */
	public void nextInterface(int buttomNum) {
		buttons[buttomNum].doPurpose();
	}
	
	/*-
	 set up the map for the game interface. depending on the small map 
	 option on or off the size of the map could be 28*18 or 14*9 
	 */
	public void setUpMap() {
		if (option.smallMap) {
			size=50;
		} else {
			size=25;
		}
		int startX=100+size;
		
		
		c.setBackgroundColor(new Color(124,252,0));
		c.clear();
		c.setColor(new Color(169,169,169));
		c.fillRect(90, 40, 720, 470);
		c.setColor(snake_game.lightGreen);
		c.fillRect(100, 50, 700, 450);
		c.setColor(snake_game.darkGreen);
		
		for (int y=50; y<500; y+=size ) {
			if (startX==100) {
				startX+=size;
			} else {
				startX-=size;
			}
			for (int x=0; x<700; x+=size*2) {
				c.fillRect(startX+x, y, size, size);
			}
		}

	}
}

/*-
 the class are used when the user are on the main menu
 it is a sub class of interface, it inherits all the none
 private method and variable in interfaces
 */
class main_menu extends interfaces{
	private selecter s;
	private boolean firstTime=true;
	private boolean onPress=false;
	private boolean enterDown=false;
	private Image title = Toolkit.getDefaultToolkit().getImage("C:\\Users\\oggog\\Pictures\\Snake.png");
	
	/*- 
	 constructor + constructor call for the super class
	 
	 precondition: 
	 	consleUsing as a Console object 
	 postcondition:
		a main_menu object made
	 */
	public main_menu(Console consoleUsing) {
		super(consoleUsing);
		int[][] buttonsPosAndSize={{390,330,120,30,1},{390,380,120,30,2},{390,430,120,30,-999}};
		String[] texts= {"Start","Option","Exit"};
		boolean[] isSelected= {true,false,false};
		setUpButtons(buttonsPosAndSize, texts, isSelected);
		s=new selecter(3,50, 520, 345, 30, 120, 390, 330, consoleUsing);
	}
	
	/*-
	 this overrides the method in interfaces it display
	 the button and everything that main_menu has. Similar
	 to all the other display method in other class
	 */
	public void display() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException{
		// check and change the button status according
		// the selecter status
		int temp=s.getAt();
		if (s.change_pos(c.getLastKeyChar())) {
			changeButtonStatus(true, temp, s.getAt());
		}
		if (c.getKeyChar()==Console.VK_ENTER) {
			changeButtonStatus(false, temp, s.getAt());
		}
		
		// display the title of the game
		c.drawImage(title, 220, 180);
		
		// update buttons and selecter
		super.display();
		s.display_selecter();
		
		
	}

	/*-
	 instead of do display and redraws everything every time.
	 Update will check for conditions and if the condition is met 
	 than calls display to redraw so the program. User interacts are included in update.
	 OnPress are there so that the selecter would jump only once when holding the key down.
	 This is similar in all other class's update method.
	 */
	public void update() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException{
		/*- 
		 firstTime means when you initially enters the interface where there
		 is nothing displayed on the console so if firstTime is true the program
		 will display the initial looking of the interface or updates anything that needs to be
		 */
		if (firstTime) {
			display();
			firstTime=!firstTime;
		} else if (c.getKeyChar()!=Console.VK_UNDEFINED && !onPress && !c.isKeyDown(Console.VK_ENTER)) {
			display();
			onPress=!onPress;
		} else if (c.getKeyChar()==Console.VK_UNDEFINED && onPress) {
			onPress=!onPress;
		} else if (c.isKeyDown(Console.VK_ENTER) && !enterDown) {
			display();
			enterDown=!enterDown;
		} else if (!c.isKeyDown(Console.VK_ENTER) && enterDown) {
			enterDown=!enterDown;
			changeButtonStatus(false, 0, s.getAt());
			nextInterface(s.getAt());
			firstTime=!firstTime;
		}		
	}
	
}

/*-
 This is the option class where option setting
 can be done here. There are many buttons representing
 different options but only the sound option are on
 on default. This inherits all the none private method 
 and variable in interfaces   
 */
class option extends interfaces{
	private selecter s;
	private boolean firstTime=true;
	private boolean onPress=false;
	private boolean enterDown=false;
	static boolean manyPoint=false;
	static boolean smallMap=false;
	static boolean soundOn=true;
	
	/*-
	 constructor + constructor call for the super class
	 
	 precondition: 
	 	consleUsing as a Console object 
	 postcondition:
		a option object made
	 */
	public option(Console consoleUsing) {
		super(consoleUsing);
		int[][] buttonsPosAndSize={{370,250,190,30,0},{370,300,190,30,0},{370,350,190,30,0},{370,400,190,30,0},{370,450,190,30,-2}};
		String[] texts= {"Music: on","Easy Mode: off","Small Map: off","Many Point: off","back"};
		boolean[] isSelected= {true,false,false,false,false};
		setUpButtons(buttonsPosAndSize, texts, isSelected);
		s=new selecter(5,50, 570, 265, 30, 190, 370, 250, consoleUsing);
	}
	
	// similar to the one that you would find in main_menu class
	public void display() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException{
		int temp=s.getAt();
		if (s.change_pos(c.getLastKeyChar())) {
			changeButtonStatus(true, temp, s.getAt());
		}
		if (c.getKeyChar()==Console.VK_ENTER) {
			changeButtonStatus(false, temp, s.getAt());
		}
		
		c.setColor(Color.black);
		c.setFont(new Font("SansSerif", Font.BOLD, 38));
		c.drawString("Option", 397, 200);
		
		super.display();
		s.display_selecter();
	}
	
	/*- 
	 similar to the one that you would find in main_menu class
	 but includes an additional code to deal with setting changing 
	 */
	public void update() throws UnsupportedAudioFileException, IOException, LineUnavailableException , InterruptedException{
		if (firstTime) {
			display();
			firstTime=!firstTime;
		} else if (c.getKeyChar()!=Console.VK_UNDEFINED && !onPress && !c.isKeyDown(Console.VK_ENTER)) {
			display();
			onPress=!onPress;
		} else if (c.getKeyChar()==Console.VK_UNDEFINED && onPress) {
			onPress=!onPress;
		} else if (c.isKeyDown(Console.VK_ENTER) && !enterDown) {
			display();
			enterDown=!enterDown;
		} else if (!c.isKeyDown(Console.VK_ENTER) && enterDown) {
			enterDown=!enterDown;
			changeButtonStatus(false, 0, s.getAt());
			
			// additional code with setting changes
			if (s.getAt()==3) {
				manyPoint=!manyPoint;
			} else if (s.getAt()==1) {
				if (snake_game.sleepTime==70) {
					snake_game.sleepTime=40;
				}else {
					snake_game.sleepTime=70;
				}
				// changes the ticktime with in the time class so time can be synchronize with real time
				time.tickTime=snake_game.sleepTime;
			} else if (s.getAt()==4) {
				firstTime=!firstTime;
			} else if (s.getAt()==2){
				smallMap=!smallMap;
			} else {
				soundOn=!soundOn;
			}
		
			display();
			nextInterface(s.getAt());
			
			
		}
	}
}

/*-
 this is the main interface for the program whereas the playing
 part of the program happens at this stage. It inherits and uses 
 methods and variable that is non private in interfaces 
 */
class game_interface extends interfaces{
	private selecter s;
	private boolean firstTime=true;
	private boolean onPress=false;
	private boolean enterDown=false;
	private boolean paused=false;
	private int pAmount, size;
	private Console c;
	private ArrayList<body> snake=new ArrayList<>();
	private point[] points=new point[5];  
	private time t;	
	private File gotAPointSound,snakeDieSound, gameEndSound, turnSound;
	static int score=-1;
	static int highestScore=0;
	
	/*-
	 constructor + constructor call for the super class
	 
	 precondition: 
	 	consleUsing as a Console object 
	 postcondition:
		a game_interface object made
	 */
	public game_interface(Console consleUsing) {
		super(consleUsing);
		c=consleUsing;
		t=new time(300, 550, new Font("SansSerif", Font.BOLD, 18), c);
		gotAPointSound = new File("C:\\Java_shits\\grade_11\\src\\classe\\project\\gotAPoint.wav");
		snakeDieSound = new File("C:\\Java_shits\\grade_11\\src\\classe\\project\\snakeDie.wav");
		gameEndSound = new File("C:\\Java_shits\\grade_11\\src\\classe\\project\\gameEnd.wav");
		turnSound= new File("C:\\Java_shits\\grade_11\\src\\classe\\project\\turnSound.wav");
	}
	
	/*-
	 it's not the same or similar to what is in main_menu
	 it display the snake on the map while checking for
	 any collision detection, if so then breaks the program
	 or increase body size and score if it is a point
	 */
	public void display() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException {
		// check for any collision when counter=1( i.e. checks for every two sleep )
		if (body.counter==1) {
			int headX=snake.get(0).getX();
			int headY=snake.get(0).getY();
			int i=0;
			
			// if the head of the snake hit the boundaries the player snake will die
			if (snake.get(0).checkBoundaries()) {
				died();
				return;
			}
			
			/*- 
			 check to see if the head of the snake hits any points if so it get eaten 
			 and the body of the snake are increase by one
			 */
			for (point p:points) {
				if (p!=null && headX==p.getX()&& headY==p.getY()) {
					p.setEaten(true);
					addBody();
					playSound(gotAPointSound);
				}
			}
			
			/*-
			 check if the head of the snake hits any parts of the snake body if so
			 the snake will die and the game will end if not it will draw the snake body
			 */
			for (body b: snake) {
				if (i!=0 && b.getX()==headX && b.getY()==headY) {
					died();
					return;
				}
				b.drawBody();
				i++;
			}
			body.counter=0;
		} else {
			body.counter++;
		}
		
		// if the point are eaten it will make a new point in a random position
		// also displays it and increase the score and displays it 
		for (point p:points) {
			if (p==null) {
				break;
			} else if (p.isEaten()) {
				p.generatePointPos();
				while (checkOverlappedPos(p)) {
					p.generatePointPos();
				}
				p.displayPoint();
				p.setEaten(false);
				score+=1;
				c.setColor(new Color(124,252,0));
				c.fillRect(155, 535, 25, 20);
				c.setColor(Color.black);
				c.setFont(new Font("SansSerif", Font.BOLD, 18));
				c.drawString("Score:", 100, 550);
				c.drawString(""+score, 160, 550);
				c.drawString("Hights Score:", 500, 550);
				c.drawString(""+highestScore, 620, 550);
			}
		}
		
		// displays some writing 
		c.setColor(Color.black);
		c.setFont(new Font("SansSerif", Font.BOLD, 18));
		c.drawString("Press P to pause/continue", 10, 25);
		c.drawString("Press E to exit the game", 270, 25);
	}
	
	/*- 
	 similar to what is in main_menu but the interaction are made for snake
	 direction change. The method here also include a timer.
	 */
	public void update() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException{
		
		if (firstTime) {
			setUpMap();
			
			if(option.manyPoint) {
				for (int i=0; i<5; i++) {
					points[i]=new point(c);
				}
			} else {
				points[0]=new point(c);
			}
			
			if (option.smallMap) {
				size=50;
			} else {
				size=25;
			}
			
			snake.add(new body('d',false,450,250,size,c));
			snake.add(new body('d',false,450-size,250,size,c));
			snake.add(new body('d',true,450-size*2,250,size,c));
			
			// resets the score to initial value
			if (option.manyPoint) {
				score=-5;
			} else {
				score=-1;
			}
			
			firstTime=!firstTime;
			
		/*- 
		 this section of else if checks for user input like snake movement,
		 pause and exiting the program
		 */	
		} else if (c.getKeyChar()!=Console.VK_UNDEFINED && !onPress) {
			char lastChar=c.getLastKeyChar();
			char dir=snake.get(0).getDirection();
			
			/*- 
			 check user input for snake turns using wasd the snake can't
			 turn around going left if it's going right and same thing for left, up 
			 and down because it does not make any sense for a snake to do a 180 turn
			 onto it self
			 */
			if ((lastChar=='a'&&dir!='d'||lastChar=='d'&&dir!='a'||lastChar=='w'&&dir!='s'||lastChar=='s'&&dir!='w')&& !paused) {
				int x= snake.get(0).getX();
				int y= snake.get(0).getY();
				snake.get(0).setDirection(lastChar);
				for (int i=0; i<snake.size(); i++) {
					snake.get(i).setTurnWaitingList(new turnWaiting(x,y,lastChar));
				}
				
				playSound(turnSound);
			} else if (lastChar=='p') {
				paused=!paused;
			} else if (lastChar=='e') {
				System.exit(1);
			}
			onPress=!onPress;
		} else if (c.getKeyChar()==Console.VK_UNDEFINED && onPress){
			onPress=!onPress;
		}
		
		// updates timer and the snake
		if (!paused) {
			t.displayTimer();
			display();
		}

		
	}
	
	// private helper method used to check for 
	// the spawn position of point so that it does not
	// spawn inside of the snake and causing problems 
	private boolean checkOverlappedPos(point p) {
		int pointX=p.getX();
		int pointY=p.getY();
		for (body b: snake) {
			if (b.getX()==pointX && b.getY()==pointY) {
				return true;
			}
		}
		body tail=snake.get(snake.size()-1);
		if (tail.getX()==pointX && tail.getY()==pointY) {
			return true;
		} else {
			return false;
		}
	}
	
	// once the snake has gotten a point this method
	// is used to initialize and add a new body to the 
	// snake
	private void addBody() {
		char dir=snake.get(snake.size()-1).getDirection();
		int tailX=snake.get(snake.size()-1).getX();
		int tailY=snake.get(snake.size()-1).getY();
		
		snake.add(snake.size()-1, new body(dir,false,tailX,tailY,size,c));
		if (dir=='d') {
			snake.get(snake.size()-1).setX(tailX-size);
		} else if (dir=='a') {
			snake.get(snake.size()-1).setX(tailX+size);
		} else if (dir=='w') {
			snake.get(snake.size()-1).setY(tailY+size);
		} else {
			snake.get(snake.size()-1).setY(tailY-size);
		}
		
		snake.get(snake.size()-1).setLightGreen(!snake.get(snake.size()-1).getIsLightGreen());
		
		for (turnWaiting tw:snake.get(snake.size()-1).getTurnWaitingList()) {
			snake.get(snake.size()-2).setTurnWaitingList(tw);
		}
	}
	
	// resets the snake body and timer and also 
	// move into the next interface when the snake die
	private void died() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException {
		playSound(snakeDieSound);
		c.setBackgroundColor(Color.white);
		// sleep here to wait for the death sound to finish before executing any codes
		Thread.sleep(1100);
		playSound(gameEndSound);
		c.clear();
		snake_game.interfaceOn+=2;
		firstTime=!firstTime;
		snake.clear();
		t.setMin(0);
		t.setSec(0);
		t.setSleepCounted(0);
		if (score>highestScore) {
			highestScore=score;
		}
		
		for (int i=0; i<5; i++) {
			points[i]=null;
		}
		
	}
	
	/*- 
	 helper method to play sound since play sound with file takes
	 a few lines of code and it is not worth it to type it repeatedly 
	 */
	private void playSound(File f) throws UnsupportedAudioFileException, IOException, LineUnavailableException{
		if (option.soundOn) {
			AudioInputStream audio = AudioSystem.getAudioInputStream(f);
		    Clip clip = AudioSystem.getClip();
		    clip.open(audio);
		    clip.start();
		}
    }
	
	/*-
	 debug use ONLY
	 */
	public String toString() {
		for (body b: snake) {
			System.out.print(b);
			for(turnWaiting tw: b.getTurnWaitingList()) {
				System.out.print(tw+" ");
			}
			System.out.println("!");
		}
		System.out.println("#################################");
		return ""; 
	}
}

/*-
 the end menu is the last interface of the program where the player
 will visit if their snake happens to die. The end menu gives player 
 a chance to decide if they wants to play again or change some options
 or exiting the program. It inherits and uses methods and variable 
 that is non private in interfaces  
*/
class end_menu extends interfaces{
	private selecter s;
	private boolean onPress=false;
	private boolean enterDown=false;
	private boolean firstTime=false;
	
	/*-
	 constructor + constructor call for the super class
	 
	 precondition: 
	 	consleUsing as a Console object 
	 postcondition:
		a end_menu object made
	 */
	public end_menu(Console consoleUsing) {
		super(consoleUsing);
		int[][] buttonsPosAndSize={{390,310,120,30,-2},{390,360,120,30,-1},{390,410,120,30,-999}};
		String[] texts= {"Again","Option", "Exit"};
		boolean[] isSelected= {true,false,false};
		setUpButtons(buttonsPosAndSize, texts, isSelected);
		s=new selecter(3,50, 520, 325, 30, 120, 390, 310, consoleUsing);
	}
	
	/*- 
	 similar to the one that you would find in main_menu class but
	 it also displays the current total score and highest score the 
	 player had
	 */
	public void display() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException {
		int temp=s.getAt();
		if (s.change_pos(c.getLastKeyChar())) {
			changeButtonStatus(true, temp, s.getAt());
		}
		if (c.getKeyChar()==Console.VK_ENTER) {
			changeButtonStatus(false, temp, s.getAt());
		}
		
		super.display();
		s.display_selecter();
		
		c.setColor(Color.black);
		c.setFont(new Font("SansSerif", Font.BOLD, 30));
		c.drawString("Your Total Score Was:", 270, 230);
		c.drawString(""+game_interface.score, 595, 230);
		c.drawString("Your Highest Score Was:", 260, 280);
		c.drawString(""+game_interface.highestScore, 620, 280);
	}
	
	/*- 
	 similar to the one that you would find in main_menu class
	*/
	public void update() throws UnsupportedAudioFileException, IOException, LineUnavailableException, InterruptedException{
		if (!firstTime) {
			display();
			firstTime=!firstTime;
		}
		
		if (c.getKeyChar()!=Console.VK_UNDEFINED && !onPress && !c.isKeyDown(Console.VK_ENTER)) {
			display();
			onPress=!onPress;
		} else if (c.getKeyChar()==Console.VK_UNDEFINED && onPress) {
			onPress=!onPress;
		} else if (c.isKeyDown(Console.VK_ENTER) && !enterDown) {
			display();
			enterDown=!enterDown;
		} else if (!c.isKeyDown(Console.VK_ENTER) && enterDown) {
			enterDown=!enterDown;
			changeButtonStatus(false, 0, s.getAt());
			nextInterface(s.getAt());
			firstTime=!firstTime;
		}		
	}
}

/*-
 this is the class for button. The class contains all the variables and 
 methods that a button needs to function. note: the class are made to
 handle only one button so to handle more then one button you would be
 to create multiple objects in the main program 
 */
class button{
	private int x;
	private int y;
	private int width;
	private int height;
	private String text;
	private boolean selected;
	private boolean pressed=false;
	private int purpose;
	Console c;
	
	/*-
	 constructor for the button class
	 
	 precondition: 
	 	int x, y for the coordinate int width, height for the button,
	 	string text for button text, boolean selected for is selected,
	 	int purpose and consleUsing as a Console object 
	 postcondition:
		a button object made
	 */
	public button(int x, int y,int width, int height,String text, boolean selected,int purpose, Console consleUsing) {
		this.x=x;
		this.y=y;
		this.width=width;
		this.height=height;
		this.text=text;
		this.selected=selected;
		this.purpose=purpose;
		c=consleUsing;
	}
	
	/*-
	this private helper method help to determine the position of the text
	with in the button so that it is in the middle of it.
	
	precondition:
		int width and int height of the button
	postcondition:
		the position of the text are found and the
		x and y value is returned as an array
	 */
	private int[] computTextPos(int width, int height) {
		int buttonHeightMid=(int)(height/2+0.5+y);
		int buttonWidthMid=(int)(width/2+0.5+x);
		
		int textPosx=(int)(buttonWidthMid-text.length()*6);
		int textPosy=buttonHeightMid+9;
		
		int[] pos={textPosx,textPosy};
		return pos;
	}
	
	/*-
	 this method display the button on the screen and also 
	 updates it when staff changes i.e the button is being
	 pressed 
	 */
	public void displayButton() {
		int[] text_pos=computTextPos(width,height);
		
		c.setColor(Color.white);
		c.fill3DRect(x, y, width, height, !selected);
		if (!pressed) {
			c.setColor(Color.green);
			c.fill3DRect(x, y, width, height, !selected);
		} else {
			c.setColor(Color.red);
			c.fill3DRect(x, y, width, height, !selected);
		}
		
		c.setFont(new Font("SansSerif", Font.BOLD, 24));
		c.setColor(Color.black);
		c.drawString(text, text_pos[0], text_pos[1]);
	}

	/*-
	 changes the button status which is
	 selected or pressed. If which is true 
	 then selected get changed else pressed 
	 get's changed
	 
	 precondition: 
	 	boolean which(which status is changing)
	 postcondition:
	 	the according status are changed
	 */
	public void changeButtonStatus(boolean which){
		if (which) {
			selected=!selected;
		} else {
			pressed=!pressed;
		}
	}
	
	/*-
	 this method here execute the purpose of the button if the button
	 has a purpose number of -999 means this button is used for exit
	 so when doPurpose it will exit the program. purpose number of 0
	 means the button is for options so doPurpose will change the on
	 and off text that is displayed. Any other purpose number means 
	 the button is used to jump into different interface the doPurpose
	 will change the static variable interfaceOn
	 */
	public void doPurpose() {
		if (purpose!=0) {
			if (purpose==-999) {
				System.exit(1);
			} else {
				snake_game.interfaceOn+=purpose;
			}
			c.clear();
		} else {
			int[] a=computTextPos(width, height);
			if (text.indexOf("on")!=-1) {
				text=text.substring(0, text.indexOf("on"))+"off";
			} else {
				text=text.substring(0, text.indexOf("off"))+"on";
			}
			displayButton();
			a=computTextPos(width, height);
		}
	}
}

/*-
 since mouse interaction in general gets very complicated
 and annoying I decided to make a selecter so user interaction 
 are limited to only keyboards. The selecter class contains all
 the methods and variables that a selecter needs to function
 */
class selecter{
	private int buttomNum, jumpDis, buttomHeight, buttomWidth, buttomX, buttomY;
	private int[] xPos=new int[3];
	private int[] yPos=new int[3];
	private int at=0;
	Console c;
	
	/*-
	 constructor for the selecter class
	 
	 precondition: 
	 	int buttomNum for the number buttons it's used for, int jumpDis
	 	for the distance between each button, int x,y for being selecter
	 	position, int buttomHeight,buttomWidth, int buttomX, buttomY and 
	 	consleUsing as a Console object 
	 postcondition:
		a selecter object made
	 */
	public selecter(int buttomNum,  int jumpDis, int x, int y,int buttomHeight, int buttomWidth,int buttomX,int buttomY, Console consleUsing) {
		this.buttomNum=buttomNum;
		this.jumpDis=jumpDis;
		this.buttomHeight=buttomHeight+6;
		this.buttomWidth=buttomWidth+6;
		this.buttomX=buttomX-3;
		this.buttomY=buttomY-3;
		xPos[0]=x;
		xPos[1]=x+30;
		xPos[2]=x+30;
		yPos[0]=y;
		yPos[1]=y-15;
		yPos[2]=y+15;	
		c=consleUsing;
	}

	public void display_selecter() {
		c.setColor(Color.red);
		c.fillPolygon(xPos, yPos, 3);
		c.drawRect(buttomX, buttomY, buttomWidth, buttomHeight);
	}
	
	private void clear_selecter() {
		c.setColor(Color.white);
		c.fillPolygon(xPos, yPos, 3);
		c.drawRect(buttomX, buttomY, buttomWidth, buttomHeight);
	}
	
	/*-
	 based on user input changes the selecter's position 
	 accordingly and re-display it
	 */
	public boolean change_pos(char k) {
		if (k=='w' && getAt()>0) {
			clear_selecter();
			for (int i = 0; i < xPos.length; i++) {
				yPos[i]-=jumpDis;
			}
			buttomY-=jumpDis;
			setAt(getAt() - 1);
			return true;
		} else if (k=='s' && getAt()+1<buttomNum) {
			clear_selecter();
			for (int i = 0; i < xPos.length; i++) {
				yPos[i]+=jumpDis;
			}
			buttomY+=jumpDis;
			setAt(getAt() + 1);
			return true;
		}
		return false;
	}

	public int getAt() {
		return at;
	}

	public void setAt(int at) {
		this.at = at;
	}	
}

/*-
 this class is for the body of the snake it can also
 be the head and the tail of the snake
 */
class body{
	private char direction;
	private boolean isTail;
	private int x, y, posBackX, posBackY, r;
	private Console c;
	private boolean isLightGreen;
	private ArrayList<turnWaiting> turnWaitingList=new ArrayList<>(); 
	static int counter=1;
	
	/*-
	 constructor for the body class
	 
	 precondition: 
	 	char direction, boolean isTail, int x,y for body starting position,
	 	int r for the size or radius, consleUsing as a Console object 
	 postcondition:
		a body object made
	 */
	public body(char direction, boolean isTail, int x, int y, int r, Console consoleUsing) {
		this.direction=direction;
		this.isTail=isTail;
		this.setX(x);
		this.setY(y);
		this.r=r;
		posBackX=-r;
		c=consoleUsing;
		
		if (option.smallMap) {
			isLightGreen=false;
		} else {
			isLightGreen=true;
		}
		
		
	}
	
	public void drawBody() {
		if (isTail) {
			if (isLightGreen) {
				c.setColor(snake_game.lightGreen);
				c.fillRect(getX()+posBackX, getY()+posBackY, r, r);
			} else {
				c.setColor(snake_game.darkGreen);
				c.fillRect(getX()+posBackX, getY()+posBackY, r, r);
			}
			setLightGreen(!isLightGreen);
		} 
		c.setColor(Color.blue);	
		c.fillOval(getX(), getY(), r, r);
		computeMove();

	}
	
	// check if the snake head hits the Boundaries of the map and if so it is died
	public boolean checkBoundaries() {
		if ((x>775 || x<100) || (y>475 || y<50)) {
			return true;
		}
		return false;
	}

 	private void computeMove() {
		checkList();
		
		if (direction=='d') {
			setX(x + r);
			posBackX=-r;
			posBackY=0;
		} else if (direction=='a') {
			setX(x - r);
			posBackX=r;
			posBackY=0;
		} else if (direction=='w') {
			setY(y - r);
			posBackX=0;
			posBackY=r;
		} else{
			setY(y + r);
			posBackX=0;
			posBackY=-r;
		}
		
	}
	
	
	public void setDirection(char direction) {
		this.direction = direction;
	}
	
	public char getDirection() {
		return direction;
	}

	public void setTurnWaitingList(turnWaiting object) {
		this.turnWaitingList.add(object);
	}
	
	public ArrayList<turnWaiting> getTurnWaitingList() {
		return turnWaitingList;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}
	
	public void setX(int x) {
		this.x = x;
	}

	public void setY(int y) {
		this.y = y;
	}
	
	/*-
	 checks if the turnWaitingList has any elements in it, if so then
	 it will change the heading of the snake to the first element in the 
	 arraylist and remove it
	 */
	public void checkList() {
		if (getTurnWaitingList().size()!=0) {
			int xPos=getTurnWaitingList().get(0).getX();
			int yPos=getTurnWaitingList().get(0).getY();
			char d=getTurnWaitingList().get(0).getDirection();
			if (x==xPos && y==yPos) {
				setDirection(d);
				turnWaitingList.remove(0);
			} 
		}
	}

	public boolean getIsLightGreen() {
		return isLightGreen;
	}
	
	public void setLightGreen(boolean isLightGreen) {
		this.isLightGreen = isLightGreen;
	}
	
	/*-
	 debug use ONLY
	 */
	public String toString() {
		return x+" "+y+" "+direction;
	}

}

/*-
  class for a point that stores information about at which point
  the snake body needs to turn and which direction it's heading  
 */
class turnWaiting{
	private int x;
	private int y;
	private char direction;
	
	/*-
	 constructor for the turnWaiting class
	 
	 precondition: 
	 	int x,y for for the position to turn, char direction for turn direction 
	 postcondition:
		a turnWaiting object made
	 */
	public turnWaiting(int x, int y, char direction) {
		this.x=x;
		this.y=y;
		this.direction=direction;
	}
	
	public char getDirection() {
		return direction;
	}

	public int getY() {
		return y;
	}

	public int getX() {
		return x;
	}
	
	/*-
	 debug use ONLY
	 */
	public String toString() {
		return "("+x+","+y+","+direction+")";
	}
}

// class for the point that the snake needs to try to eat to increase the score and body size
class point{
	private int x;
	private int y;
	private boolean eaten=true;
	private Console c;
	private Image apple = Toolkit.getDefaultToolkit().getImage("C:\\Java_shits\\grade_11\\src\\classe\\project\\pointAppleImage.png");
	
	/*-
	 constructor for the point class
	 
	 precondition: 
	 	Console consoleUsing for the console currently on use
	 postcondition:
		a point object made
	 */
	public point(Console consoleUsing) {
		c=consoleUsing;
	}
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
	
	public void generatePointPos() {
		x= ((int)(Math.random()*700/interfaces.size-1)+1)*interfaces.size+100;
		y= ((int)(Math.random()*450/interfaces.size-1)+1)*interfaces.size+50;
	}
	
	public void displayPoint() {
		c.setColor(Color.yellow);
		c.drawImage(apple, x+3, y,interfaces.size-6,interfaces.size);
//		c.fillOval(x, y, interfaces.size, interfaces.size);
	}

	public boolean isEaten() {
		return eaten;
	}

	public void setEaten(boolean eaten) {
		this.eaten = eaten;
	}
}

/*-
 this is my home made time class to track and display the time. There is possibly
 a built in time class but I still made my own since I think it is more flexible to
 use the class
 */
class time{
	static int tickTime;
	private final int oneSec=1000;
	private final int oneMin=60;
	private int sleepCounted;
	private int sec=0;
	private int min=0;
	private int timerX;
	private int timerY;
	private Font timerFont;
	private Console c;
	
	/*-
	 constructor for the time class
	 
	 precondition: 
	 	int timerX,timerY for timer position, Font timerFont and
	 	Console consoleUsing for the console currently on use
	 postcondition:
		a time object made
	 */
	public time( int timerX, int timerY, Font timerFont, Console consoleUsing) {
		tickTime=snake_game.sleepTime;
		this.timerX=timerX;
		this.timerY=timerY;
		this.timerFont=timerFont;
		c=consoleUsing;
	}
	
	/*- 
	 the timer tick when ever a sleep cycle is done and the amount
	 of ms the time ticks is depending on the length of the sleep
	 time of the program it self
	 */
	private void tick() {
		setSleepCounted(sleepCounted + tickTime);
		computTime();	
	}
	
	private void computTime() {
		sec = sec + sleepCounted/oneSec;
		setSleepCounted(sleepCounted % oneSec);
		setMin(min + sec/oneMin);
		sec = sec % oneMin;		
	}
	
	public void displayTimer() {
		c.setColor(new Color(124,252,0));
		c.fillRect(timerX, timerY-24, 141, 27);
		c.setColor(Color.black);
		c.drawString("Timer: "+min+":"+sec, timerX, timerY);
		tick();
	}

	public void setSleepCounted(int sleepCounted) {
		this.sleepCounted = sleepCounted;
	}

	public void setSec(int sec) {
		this.sec=sec;
	}

	public void setMin(int min) {
		this.min = min;
	}
}