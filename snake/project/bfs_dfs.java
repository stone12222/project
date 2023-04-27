package classe.project;

import java.awt.Color;
import java.awt.Font;

import hsa_ufa.Console;

public class bfs_dfs {
	public static void main(String[] args) throws InterruptedException {
		Console c=new Console(1000,650);
		c.enableMouse();
	    c.enableMouseMotion();
		constructionTool ct=new constructionTool(c);
		
		ct.toolBarCons();
		
		while(true) {
			synchronized(c) {
			ct.construct();
			}
			Thread.sleep(25);
		}
	}
}

class bfs{
	
}

class constructionTool{
	private Console c;
	private int mouseClick;
	private int mouseOldX=0;
	private int mouseOldY=0;
	private int counter=0;
	private int[] toolNodeCentre= {775,95};
	private boolean nodeSelected=false;
	private boolean linkSelected=false;
	private Node n;
	private Link l;
	
	public constructionTool(Console consoleUsing) {
		c=consoleUsing;
	}
	
	public void toolBarCons() {
		c.setColor(Color.lightGray);
		c.fill3DRect(700, 0, 300, 650, true);
		
		c.setColor(Color.yellow);
		c.fillOval(750, 70, 50, 50);
		c.setColor(Color.red);
		c.drawLine(900, 70, 950, 120);
		c.drawLine(750, 180, 800, 230);
		
		c.setColor(Color.black);
		c.setFont(new Font("SansSerif", Font.BOLD, 30));
		c.drawString("Tool Bar:", 780, 25);
		c.setFont(new Font("SansSerif", Font.BOLD, 25));
		c.drawString("e", 768, 103);
		c.setFont(new Font("SansSerif", Font.BOLD, 18));
		c.drawString("Node", 755, 138);
		c.drawString("Link", 905, 138);
		c.drawString("n", 775, 200);
		c.drawString("Link with dis", 740, 255);
	}
	
	public void construct() {
		mouseClick = c.getMouseClick();
		int x=c.getMouseX();
		int y=c.getMouseY();
		
		if (mouseClick!=0) {
			// for tool bar
			if (sqrt(pow((x-toolNodeCentre[0]),2)+pow((y-toolNodeCentre[1]),2))<=25) {
				nodeSelected=!nodeSelected;
			} else if (x>=900 && x<=950 && y>=70 && y<=120) {
				linkSelected=!linkSelected;
			}
			
			// for initial
			if (nodeSelected) {
				if (x<=670) {
					n=new Node(x-25, y-25, c);
					n.showNode();
					nodeSelected=!nodeSelected;
				}
			} else if (linkSelected) {
				if (x<=695) {
					System.out.println(l);
					if (counter==0) {
						l=new Link(x, y, c);
					} else {
						counter=0;
						l.setEndX(x);
						l.setEndY(y);
						l.showLink();
						linkSelected=!linkSelected;
					}
					counter++;
					
				}
			}
		} 
		
		mouseOldX=x;
		mouseOldY=y;
	}
	
	private double sqrt(double e) {
		return Math.sqrt(e);
	}
	
	private double pow(double e, double based) {
		return Math.pow(e, based);
	}
	
}

class Node {
	private int x;
	private int y;
	private String word;
	private Console c;
	public static int nodeNum=1;
	
	public Node(int x,int y,Console consoleUsing) {
		this.x=x;
		this.y=y;
		word="E"+nodeNum;
		c=consoleUsing;
		nodeNum+=1;
	}
	
	public void showNode() {
		c.setColor(Color.yellow);
		c.fillOval(x, y, 50, 50);
		c.setColor(Color.black);
		int[] wordXY=computTextPos(50, 50);
		c.drawString(word, wordXY[0], wordXY[1]);
	}
	
	/*-
	this private helper method help to determine the position of the text
	with in the button so that it is in the middle of it.
	 */
	private int[] computTextPos(int width, int height) {
		int buttonHeightMid=(int)(height/2+0.5+y);
		int buttonWidthMid=(int)(width/2+0.5+x);
		
		int textPosx=(int)(buttonWidthMid-word.length()*6);
		int textPosy=buttonHeightMid+7;
		
		int[] pos={textPosx,textPosy};
		return pos;
	}
}

class Link{
	private Console c;
	private int startX;
	private int startY;
	private int endX;
	private int endY;
	
	public Link(int x, int y, Console consoleUsing) {
		setStartX(x);
		setStartY(y);
		c=consoleUsing;
	}

	public void setStartY(int startY) {
		this.startY = startY;
	}

	public void setStartX(int startX) {
		this.startX = startX;
	}

	public void setEndX(int endX) {
		this.endX = endX;
	}

	public void setEndY(int endY) {
		this.endY = endY;
	}
	
	public void showLink() {
		c.setColor(Color.red);
		c.drawLine(startX, startY, endX, endY);
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return startX+" "+startY;
	}
}