#Import Library
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Imports successful!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
w,h= 500,500

#fungsi objek badan
def Kelinci1():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah1
    glVertex2f(58, 100) #C
    glVertex2f(68, 111) #D
    glVertex2f(84, 121) #E
    glVertex2f(104, 128) #F
    glVertex2f(117, 129) #G
    glVertex2f(135, 129) #H
    glVertex2f(150, 126) #I
    glVertex2f(162, 121) #J
    glVertex2f(171, 118) #K
    glVertex2f(182, 111) #L
    glVertex2f(191, 101) #M
    glVertex2f(197, 90) #N
    glVertex2f(200, 77) #O
    glVertex2f(198, 65) #P
    glVertex2f(193, 52) #Q
    glVertex2f(183, 41) #R
    glVertex2f(169, 31) #S
    glVertex2f(150, 24) #T
    glVertex2f(132, 21) #U
    glVertex2f(111, 22) #V
    glVertex2f(89, 27) #W
    glVertex2f(71, 37) #Z
    glVertex2f(60, 48) #A_1
    glVertex2f(53, 60) #B_1
    glVertex2f(50, 73) #C_1
    glVertex2f(52, 88) #D_1
    glEnd()

    #Telinga Kiri1
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(78, 119) #E_1
    glVertex2f(65, 151) #F_1
    glVertex2f(61, 163) #G_1
    glVertex2f(62, 173) #H_1
    glVertex2f(67, 183) #I_1
    glVertex2f(76, 190) #J_1
    glVertex2f(86, 192) #K_1
    glVertex2f(96, 192) #L_1
    glVertex2f(105, 187) #M_1
    glVertex2f(112, 179) #N_1
    glVertex2f(115, 171) #O_1
    glVertex2f(117, 158) #P_1
    glVertex2f(119, 130) #Q_1
    glEnd()

    #Telinga Kanan1
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(134, 130) #R_1
    glVertex2f(135, 167) #S_1
    glVertex2f(137, 177) #T_1
    glVertex2f(142, 184) #U_1
    glVertex2f(151, 190) #V_1
    glVertex2f(161, 192) #W_1
    glVertex2f(171, 191) #Z_1
    glVertex2f(180, 185) #A_2
    glVertex2f(186, 178) #B_2
    glVertex2f(189, 171) #C_2
    glVertex2f(189, 165) #D_2
    glVertex2f(187, 153) #E_2
    glVertex2f(177, 129) #F_2
    glVertex2f(172, 117) #G_2
    glEnd()

def Kelinci2():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah2
    glVertex2f(358, 100) #H_2
    glVertex2f(370, 112) #I_2
    glVertex2f(384, 121) #J_2
    glVertex2f(402, 126) #K_2
    glVertex2f(415, 128) #L_2
    glVertex2f(436, 128) #M_2
    glVertex2f(454, 123) #N_2
    glVertex2f(467, 118) #O_2
    glVertex2f(478, 112) #P_2
    glVertex2f(488, 102) #Q_2
    glVertex2f(495, 92) #R_2
    glVertex2f(499, 80) #S_2
    glVertex2f(498, 67) #T_2
    glVertex2f(494, 53) #U_2
    glVertex2f(485, 43) #V_2
    glVertex2f(472, 32) #W_2
    glVertex2f(455, 24) #Z_2
    glVertex2f(435, 20) #A_3
    glVertex2f(412, 20) #B_3
    glVertex2f(392, 25) #C_3
    glVertex2f(374, 33) #D_3
    glVertex2f(360, 45) #E_3
    glVertex2f(352, 58) #F_3
    glVertex2f(349, 72) #G_3
    glVertex2f(351, 87) #H_3
    glEnd()

    #Telinga Kiri2
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(375, 115) #I_3
    glVertex2f(363, 152) #J_3
    glVertex2f(360, 163) #K_3
    glVertex2f(363, 176) #L_3
    glVertex2f(371, 186) #M_3
    glVertex2f(380, 190) #N_3
    glVertex2f(391, 191) #O_3
    glVertex2f(400, 188) #P_3
    glVertex2f(407, 184) #Q_3
    glVertex2f(412, 177) #R_3
    glVertex2f(415, 170) #S_3
    glVertex2f(416, 158) #T_3
    glVertex2f(415, 125) #U_3
    glEnd()

    #Telinga Kanan2
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(432, 125) #V_3
    glVertex2f(434, 163) #W_3
    glVertex2f(436, 175) #Z_3
    glVertex2f(443, 184) #A_4
    glVertex2f(453, 190) #B_4
    glVertex2f(464, 191) #C_4
    glVertex2f(473, 188) #D_4
    glVertex2f(479, 185) #E_4
    glVertex2f(484, 179) #F_4
    glVertex2f(488, 171) #G_4
    glVertex2f(489, 164) #H_4
    glVertex2f(487, 153) #I_4
    glVertex2f(480, 135) #J_4
    glVertex2f(471, 116) #K_4
    glEnd()

def Kelinci3():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah3
    glVertex2f(58, 400) #L_4
    glVertex2f(69, 411) #M_4
    glVertex2f(85, 421) #N_4
    glVertex2f(101, 426) #O_4
    glVertex2f(115, 428) #P_4
    glVertex2f(135, 428) #Q_4
    glVertex2f(153, 423) #R_4
    glVertex2f(167, 418) #S_4
    glVertex2f(176, 413) #T_4
    glVertex2f(189, 401) #U_4
    glVertex2f(196, 389) #V_4
    glVertex2f(199, 377) #W_4
    glVertex2f(198, 365) #Z_4
    glVertex2f(194, 355) #A_5
    glVertex2f(188, 346) #B_5
    glVertex2f(178, 336) #C_5
    glVertex2f(162, 326) #D_5
    glVertex2f(142, 321) #E_5
    glVertex2f(122, 319) #F_5
    glVertex2f(101, 322) #G_5
    glVertex2f(85, 327) #H_5
    glVertex2f(71, 336) #I_5
    glVertex2f(60, 346) #J_5
    glVertex2f(53, 357) #K_5
    glVertex2f(50, 367) #L_5
    glVertex2f(50, 380) #M_5
    glVertex2f(53, 392) #N_5
    glEnd()

    #Telinga Kiri3
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(75, 415) #O_5
    glVertex2f(62, 455) #P_5
    glVertex2f(60, 464) #Q_5
    glVertex2f(62, 474) #R_5
    glVertex2f(68, 484) #S_5
    glVertex2f(78, 489) #T_5
    glVertex2f(87, 491) #U_5
    glVertex2f(97, 490) #V_5
    glVertex2f(103, 486) #W_5
    glVertex2f(110, 480) #Z_5
    glVertex2f(113, 473) #A_6
    glVertex2f(116, 462) #B_6
    glVertex2f(117, 446) #C_6
    glVertex2f(115, 428) #D_6
    glEnd()

    #Telinga Kanan3
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(131, 428) #E_6
    glVertex2f(133, 464) #F_6
    glVertex2f(137, 476) #G_6
    glVertex2f(144, 484) #H_6
    glVertex2f(152, 489) #I_6
    glVertex2f(161, 491) #J_6
    glVertex2f(170, 490) #K_6
    glVertex2f(178, 485) #L_6
    glVertex2f(184, 478) #M_6
    glVertex2f(188, 470) #N_6
    glVertex2f(189, 462) #O_6
    glVertex2f(186, 452) #P_6
    glVertex2f(177, 430) #Q_6
    glVertex2f(171, 416) #R_6
    glEnd()


#Fungsi Iterasi untuk looping keseluruhan program agar workspace tidak hilang tiba-tiba
def iterate():
    glViewport(50, 100, 300, 300) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #untuk membersihkan layar
    glLoadIdentity() #untuk mereset semua posisi grafik stsu bentuk
    iterate() #fungsi looping
    Kelinci1()
    Kelinci2()
    Kelinci3()
    glutSwapBuffers() #untuk membersihkan layar


#Inisialisasi  
glutInit() #inilisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #mengatur layar supaya memunculkan warna 
glutInitWindowSize(900, 900) #untuk mengatur ukuran window
glutInitWindowPosition(250, 0) #untuk mengaatur posisi layar atau window untuk workspace 
wind = glutCreateWindow("BERUANGKTH") #untuk memberi nama pada window
glutDisplayFunc(showScreen) #untuk menampilkan object yang telah dibuat pada layar, fungsi callback
glutIdleFunc(showScreen) #membuat opengl terbuka dan menampilkan objek
glutMainLoop() #untuk menilai segalanya dan untuk looping objek

#Gerak Objek
initRotAngle = 0.0
def Rotate():
    global initRotAngle
    glPushMatrix()
    glRotate(initRotAngle, 0, 0, 1)
    Kelinci1()
    Kelinci2()
    initRotAngle = initRotAngle -1
    glPopMatrix()
    glFlush()

def Timer():
    glutPostRedisplay()
    glutTimerFunc(20, Timer, 10)
    glFlush()

def Render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(160, 89, 201)
    Rotate()
    glFlush()