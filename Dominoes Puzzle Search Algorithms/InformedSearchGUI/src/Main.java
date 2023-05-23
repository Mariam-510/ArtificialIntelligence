import org.jpl7.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.lang.Integer;
import java.util.Map;
import java.util.Vector;
import java.lang.String;

class Main
{
    public static void main(String[] args)
    {
        new Input();
    }
}

class Input implements ActionListener {
    JTextField t1, t2, t3, t4, t5, t6;
    JLabel l1,l2,l3,l4,l5,l6;
    JButton b1;
    Input()
    {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        l1=new JLabel("M:" );
        l1.setBounds(100,50, 50,20);
        t1 = new JTextField();
        t1.setBounds(120, 50, 50, 20);

        l3=new JLabel("X1:" );
        l3.setBounds(100,100, 50,20);
        t3 = new JTextField();
        t3.setBounds(120, 100, 50, 20);

        l5=new JLabel("X2:" );
        l5.setBounds(100,150, 50,20);
        t5 = new JTextField();
        t5.setBounds(120, 150, 50, 20);

        l2=new JLabel("N:" );
        l2.setBounds(280,50, 50,20);
        t2 = new JTextField();
        t2.setBounds(300, 50, 50, 20);

        l4=new JLabel("Y1:" );
        l4.setBounds(280,100, 50,20);
        t4 = new JTextField();
        t4.setBounds(300, 100, 50, 20);

        l6=new JLabel("Y2:" );
        l6.setBounds(280,150, 50,20);
        t6 = new JTextField();
        t6.setBounds(300, 150, 50, 20);

        b1 = new JButton("Solve");
        b1.setBounds(190, 200, 70, 30);

        b1.addActionListener(this);

        frame.add(t1);frame.add(t2);frame.add(t3);frame.add(t4);frame.add(t5);frame.add(t6);
        frame.add(l1);frame.add(l2);frame.add(l3);frame.add(l4);frame.add(l5);frame.add(l6);
        frame.add(b1);

        frame.setSize(500, 500);
        frame.setLayout(null);
        frame.setVisible(true);

    }

    public void actionPerformed(ActionEvent e)
    {
        String M = t1.getText();
        String N = t2.getText();
        String X1 = t3.getText();
        String Y1 = t4.getText();
        String X2 = t5.getText();
        String Y2 = t6.getText();
        String lists;

        if (e.getSource() == b1)
        {
            Query q1 = new Query("consult('InformedSearch.pl')");
            q1.hasSolution();

            q1 = new Query("go(["+M+","+N+"],["+X1+","+Y1+"],["+X2+","+Y2+"],Output).");

            Map<String, Term> res1 = q1.oneSolution();

            lists="";
            for (Map.Entry<String, Term> ent : res1.entrySet())
            {
                lists = String.valueOf(ent.getValue());
                System.out.println(lists);
            }

            Vector<Character> list=new Vector<Character>();
            Vector<Vector<Character>> lists_updated=new Vector<Vector<Character>>();
            int finish = 0;
            int n=0;
            for (int i = 1; i < lists.length() - 1; i++) {
                if (Character.compare(lists.charAt(i),'[')==0 || Character.compare(lists.charAt(i),']')==0) {
                    finish++;
                    if(finish==2)
                    {
                        lists_updated.add(new Vector<Character>(list));
                        list.clear();

                        finish=0;
                    }
                }
                else if(Character.compare(lists.charAt(i),',')!=0 && Character.compare(lists.charAt(i),' ')!=0)
                {
                    if(finish==1)
                        list.add(lists.charAt(i));

                }
            }
            int x=lists.length()-2;
            String num_dom="";
            int numOfDominoes=0;
            if(Character.compare(lists.charAt(x),']')!=0)
            {
                while (Character.compare(lists.charAt(x),']')!=0 && Character.compare(lists.charAt(x),' ')!=0 && Character.compare(lists.charAt(x),',')!=0  )
                {
                    num_dom=lists.charAt(x)+num_dom;
                    x--;
                }
                numOfDominoes = java.lang.Integer.parseInt(num_dom) ;
                System.out.println(numOfDominoes);
            }

            for (int i=0;i<lists_updated.size();i++) {
                System.out.println(lists_updated.get(i));
            }

            int M1=Integer.parseInt(M);
            int N1=Integer.parseInt(N);

            new Output(M1,N1,lists_updated,num_dom);

        }
    }
}

class Output {
    int x=0;
    int y=40;
    int n = 0;
    int numofBoard = 4;
    Output(int M,int N,Vector<Vector<Character>> vecs,String num_dom)
    {
        JFrame frame = new JFrame();
        Vector<JButton> buttons=new Vector<JButton>();
        JLabel l = new JLabel();
        l.setText(num_dom+" is maximum number of dominoes that can be placed.");
        l.setBounds(20,20, 500,50);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        for (int c=0;c<vecs.size();c++)
        {
            numofBoard--;
            Vector<Character> vec = vecs.get(c);
            for (int i=0;i<M;i++)
            {
                x=n;
                y+=35;
                for (int j=0;j<N;j++)
                {
                    x+=35;//100
                    JButton b1;
                    if(vec.get(i*N+j)=='0')
                    {
                        b1=new JButton();
                        b1.setBackground(Color.WHITE);
                        b1.setBounds(x,y,35,35);
                        buttons.add(b1);

                    }
                    else if(vec.get(i*N+j)=='b')
                    {
                        b1=new JButton(new ImageIcon("Bumb.jpg"));
                        b1.setBackground(Color.WHITE);
                        b1.setBounds(x,y,35,35);
                        buttons.add(b1);
                    }
                    else if(vec.get(i*N+j)=='1')
                    {
                        b1=new JButton(new ImageIcon("DominoeRight.jpg"));
                        b1.setBackground(Color.WHITE);
                        vec.set(i*N+j+1,'x');
                        b1.setBounds(x,y,70,35);
                        buttons.add(b1);
                    }
                    else if(vec.get(i*N+j)=='2')
                    {
                        b1=new JButton(new ImageIcon("DominoeUp.jpg"));
                        b1.setBackground(Color.WHITE);
                        vec.set(i*N+j+N,'x');
                        b1.setBounds(x,y,35,70);
                        buttons.add(b1);
                    }
                }
            }
            if (numofBoard==0)
            {
                numofBoard = 4;
                n = 0;
                y+=10*(M+1);
            }
            else
            {
                n += 35*(N+1);
                y -= (35*M);
            }
        }

        frame.add(l);
        for (int i=0;i<buttons.size();i++)
        {
            frame.add(buttons.get(i));
        }
        frame.setSize(1000, 1000);
        frame.setLayout(null);
        frame.setVisible(true);

    }

}