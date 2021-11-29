#Import Library
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Imports successful!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


merah = 160
hijau = 89
biru = 201
angle_time = 0

#fungsi objek badan
def Kelinci1():
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
    
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
    glPopMatrix()

    #Telinga Kiri1
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
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
    glPopMatrix()

    #Telinga Kanan1
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
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
    glPopMatrix()

def Kelinci2():
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)

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
    glPopMatrix()

    #Telinga Kiri2
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
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
    glPopMatrix()

    #Telinga Kanan2
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
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
    glPopMatrix()

def Kelinci3():
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)

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
    glPopMatrix()

    #Telinga Kiri3
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
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
    glPopMatrix()

    #Telinga Kanan3
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
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
    glPopMatrix()

def Kelinci4():
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)

    #Wajah4
    glVertex2f(358, 400) #S_6
    glVertex2f(371, 413) #T_6
    glVertex2f(384, 420) #U_6
    glVertex2f(398, 426) #V_6
    glVertex2f(415, 428) #W_6
    glVertex2f(435, 428) #Z_6
    glVertex2f(451, 424) #A_7
    glVertex2f(467, 418) #B_7
    glVertex2f(475, 414) #C_7
    glVertex2f(483, 407) #D_7
    glVertex2f(490, 399) #E_7
    glVertex2f(496, 391) #F_7
    glVertex2f(498, 381) #G_7
    glVertex2f(499, 373) #H_7
    glVertex2f(498, 364) #I_7
    glVertex2f(495, 355) #J_7
    glVertex2f(488, 345) #K_7
    glVertex2f(476, 335) #L_7
    glVertex2f(462, 327) #M_7
    glVertex2f(449, 323) #N_7
    glVertex2f(434, 320) #O_7
    glVertex2f(419, 320) #P_7
    glVertex2f(400, 322) #Q_7
    glVertex2f(384, 328) #R_7
    glVertex2f(368, 338) #S_7
    glVertex2f(358, 349) #T_7
    glVertex2f(352, 359) #U_7
    glVertex2f(350, 370) #V_7
    glVertex2f(350, 380) #W_7
    glVertex2f(353, 392) #Z_7
    glEnd()
    glPopMatrix()

    #Telinga Kiri4
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
    glVertex2f(378, 417) #A_8
    glVertex2f(363, 450) #B_8
    glVertex2f(361, 460) #C_8
    glVertex2f(361, 468) #D_8
    glVertex2f(364, 476) #E_8
    glVertex2f(369, 484) #F_8
    glVertex2f(376, 488) #G_8
    glVertex2f(385, 491) #H_8
    glVertex2f(394, 491) #I_8
    glVertex2f(402, 487) #J_8
    glVertex2f(409, 481) #K_8
    glVertex2f(413, 474) #L_8
    glVertex2f(416, 465) #M_8
    glVertex2f(417, 445) #N_8
    glVertex2f(418, 428) #O_8
    glEnd()
    glPopMatrix()

    #Telinga Kanan4
    glPushMatrix()
    glRotated(angle_time,0,0,1)
    glScaled(3, 3, 0)
    glColor3ub(merah, hijau, biru)
    glBegin(GL_POLYGON)
    glVertex2f(432, 428) #P_8
    glVertex2f(433, 461) #Q_8
    glVertex2f(437, 475) #R_8
    glVertex2f(442, 484) #S_8
    glVertex2f(452, 489) #T_8
    glVertex2f(463, 491) #U_8
    glVertex2f(473, 488) #V_8
    glVertex2f(481, 483) #W_8
    glVertex2f(486, 476) #Z_8
    glVertex2f(488, 468) #A_9
    glVertex2f(488, 460) #B_9
    glVertex2f(485, 449) #C_9
    glVertex2f(477, 428) #D_9
    glVertex2f(471, 416) #E_9
    glEnd()
    glPopMatrix()

def Kelinci5():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah5
    glVertex2f(660, 400) #R_11
    glVertex2f(671, 412) #S_11
    glVertex2f(685, 419) #T_11
    glVertex2f(701, 425) #U_11
    glVertex2f(714, 427) #V_11
    glVertex2f(736, 427) #W_11
    glVertex2f(754, 422) #Z_11
    glVertex2f(768, 417) #A_12
    glVertex2f(779, 411) #B_12
    glVertex2f(791, 399) #C_12
    glVertex2f(798, 386) #D_12
    glVertex2f(800, 374) #E_12
    glVertex2f(798, 363) #F_12
    glVertex2f(794, 351) #G_12
    glVertex2f(781, 337) #H_12
    glVertex2f(764, 326) #I_12
    glVertex2f(745, 321) #J_12
    glVertex2f(727, 319) #K_12
    glVertex2f(711, 320) #L_12
    glVertex2f(688, 326) #M_12
    glVertex2f(674, 334) #N_12
    glVertex2f(663, 343) #O_12
    glVertex2f(656, 353) #P_12
    glVertex2f(651, 365) #Q_12
    glVertex2f(650, 379) #R_12
    glVertex2f(654, 392) #S_12
    glEnd()

    #Telinga Kiri5
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(679, 416) #T_12
    glVertex2f(666, 446) #U_12
    glVertex2f(662, 460) #V_12
    glVertex2f(662, 470) #W_12
    glVertex2f(666, 479) #Z_12
    glVertex2f(673, 485) #A_13
    glVertex2f(681, 489) #B_13
    glVertex2f(690, 491) #C_13
    glVertex2f(699, 489) #D_13
    glVertex2f(706, 485) #E_13
    glVertex2f(711, 479) #F_13
    glVertex2f(715, 472) #G_13
    glVertex2f(716, 464) #H_13
    glVertex2f(717, 455) #I_13
    glVertex2f(719, 428) #J_13
    glEnd()

    #Telinga Kanan5
    glBegin(GL_POLYGON)
    glColor3ub(160,89,201)
    glVertex2f(732, 428) #K_13
    glVertex2f(734, 462) #L_13
    glVertex2f(737, 474) #M_13
    glVertex2f(743, 483) #N_13
    glVertex2f(753, 489) #O_13
    glVertex2f(762, 490) #P_13
    glVertex2f(770, 490) #Q_13
    glVertex2f(777, 486) #R_13
    glVertex2f(783, 481) #S_13
    glVertex2f(788, 473) #T_13
    glVertex2f(789, 465) #U_13
    glVertex2f(789, 457) #V_13
    glVertex2f(783, 442) #W_13
    glVertex2f(772, 415) #Z_13
    glEnd()

def Kelinci6():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah6
    glVertex2f(660, 100) #F_9
    glVertex2f(671, 111) #G_9
    glVertex2f(684, 118) #H_9
    glVertex2f(698, 123) #I_9
    glVertex2f(713, 126) #J_9
    glVertex2f(734, 126) #K_9
    glVertex2f(749, 122) #L_9
    glVertex2f(767, 116) #M_9
    glVertex2f(777, 110) #N_9
    glVertex2f(788, 100) #O_9
    glVertex2f(794, 92) #P_9
    glVertex2f(797, 82) #Q_9
    glVertex2f(799, 73) #R_9
    glVertex2f(798, 61) #S_9
    glVertex2f(793, 51) #T_9
    glVertex2f(786, 41) #U_9
    glVertex2f(774, 32) #V_9
    glVertex2f(760, 24) #W_9
    glVertex2f(742, 19) #Z_9
    glVertex2f(721, 18) #A_10
    glVertex2f(700, 20) #B_10
    glVertex2f(681, 28) #C_10
    glVertex2f(667, 36) #D_10
    glVertex2f(657, 47) #E_10
    glVertex2f(652, 58) #F_10
    glVertex2f(649, 69) #G_10
    glVertex2f(650, 82) #H_10
    glVertex2f(654, 92) #I_10
    glEnd()

    #Telinga Kiri6
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(678, 115) #J_10
    glVertex2f(667, 139) #K_10
    glVertex2f(661, 157) #L_10
    glVertex2f(661, 165) #M_10
    glVertex2f(663, 174) #N_10
    glVertex2f(669, 182) #O_10
    glVertex2f(678, 188) #P_10
    glVertex2f(687, 189) #Q_10
    glVertex2f(697, 188) #R_10
    glVertex2f(705, 183) #S_10
    glVertex2f(711, 177) #T_10
    glVertex2f(714, 169) #U_10
    glVertex2f(716, 155) #V_10
    glVertex2f(717, 137) #W_10
    glVertex2f(718, 126) #Z_10
    glEnd()

    #Telinga Kanan6
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(731, 126) #A_11
    glVertex2f(733, 161) #B_11
    glVertex2f(736, 172) #C_11
    glVertex2f(740, 179) #D_11
    glVertex2f(746, 185) #E_11
    glVertex2f(754, 188) #F_11
    glVertex2f(761, 189) #G_11
    glVertex2f(769, 188) #H_11
    glVertex2f(775, 185) #I_11
    glVertex2f(781, 180) #J_11
    glVertex2f(785, 175) #K_11
    glVertex2f(787, 169) #L_11
    glVertex2f(788, 163) #M_11
    glVertex2f(787, 155) #N_11
    glVertex2f(783, 142) #O_11
    glVertex2f(776, 124) #P_11
    glVertex2f(771, 114) #Q_11
    glEnd()
    
def Kelinci7():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah7
    glVertex2f(959, 400) #I_18
    glVertex2f(969, 410) #J_18
    glVertex2f(981, 418) #K_18
    glVertex2f(1000, 426) #L_18
    glVertex2f(1016, 428) #M_18
    glVertex2f(1035, 428) #N_18
    glVertex2f(1051, 424) #O_18
    glVertex2f(1068, 418) #P_18
    glVertex2f(1078, 412) #Q_18
    glVertex2f(1088, 402) #R_18
    glVertex2f(1096, 391) #S_18
    glVertex2f(1100, 380) #T_18
    glVertex2f(1099, 365) #U_18
    glVertex2f(1094, 352) #V_18
    glVertex2f(1085, 341) #W_18
    glVertex2f(1071, 331) #Z_18
    glVertex2f(1052, 323) #A_19
    glVertex2f(1031, 320) #B_19
    glVertex2f(1008, 321) #C_19
    glVertex2f(990, 326) #D_19
    glVertex2f(973, 335) #E_19
    glVertex2f(958, 349) #F_19
    glVertex2f(952, 362) #G_19
    glVertex2f(950, 374) #H_19
    glVertex2f(952, 388) #I_19
    glEnd()

    #Telinga Kiri7
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(978, 418) #J_19
    glVertex2f(965, 448) #K_19
    glVertex2f(962, 460) #L_19
    glVertex2f(962, 469) #M_19
    glVertex2f(965, 477) #N_19
    glVertex2f(972, 485) #O_19
    glVertex2f(980, 490) #P_19
    glVertex2f(989, 491) #Q_19
    glVertex2f(998, 490) #R_19
    glVertex2f(1005, 486) #S_19
    glVertex2f(1011, 479) #T_19
    glVertex2f(1015, 471) #U_19
    glVertex2f(1016, 461) #V_19
    glVertex2f(1018, 443) #W_19
    glVertex2f(1019, 428) #Z_19
    glEnd()

    #Telinga Kanan7
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(1032, 428) #A_20
    glVertex2f(1035, 466) #B_20
    glVertex2f(1038, 477) #C_20
    glVertex2f(1044, 484) #D_20
    glVertex2f(1052, 489) #E_20
    glVertex2f(1062, 491) #F_20
    glVertex2f(1071, 489) #G_20
    glVertex2f(1079, 485) #H_20
    glVertex2f(1084, 479) #I_20
    glVertex2f(1088, 472) #J_20
    glVertex2f(1089, 463) #K_20
    glVertex2f(1088, 454) #L_20
    glVertex2f(1080, 433) #M_20
    glVertex2f(1072, 416) #N_20
    glEnd()

def Kelinci8():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah8
    glVertex2f(960, 100) #A_14
    glVertex2f(971, 111) #B_14
    glVertex2f(983, 119) #C_14
    glVertex2f(996, 124) #D_14
    glVertex2f(1014, 128) #E_14
    glVertex2f(1036, 127) #F_14
    glVertex2f(1052, 123) #G_14
    glVertex2f(1067, 118) #H_14
    glVertex2f(1078, 111) #I_14
    glVertex2f(1089, 102) #J_14
    glVertex2f(1096, 90) #K_14
    glVertex2f(1100, 77) #L_14
    glVertex2f(1099, 64) #M_14
    glVertex2f(1092, 50) #N_14
    glVertex2f(1080, 37) #O_14
    glVertex2f(1063, 26) #P_14
    glVertex2f(1044, 21) #Q_14
    glVertex2f(1025, 19) #R_14
    glVertex2f(1003, 21) #S_14
    glVertex2f(984, 28) #T_14
    glVertex2f(967, 39) #U_14
    glVertex2f(957, 51) #V_14
    glVertex2f(950, 66) #W_14
    glVertex2f(951, 83) #Z_14
    glEnd()

    #Telinga Kiri8
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(979, 116) #A_15
    glVertex2f(966, 146) #B_15
    glVertex2f(962, 159) #C_15
    glVertex2f(961, 168) #D_15
    glVertex2f(966, 179) #E_15
    glVertex2f(974, 186) #F_15
    glVertex2f(982, 190) #G_15
    glVertex2f(991, 191) #H_15
    glVertex2f(1002, 187) #I_15
    glVertex2f(1009, 182) #J_15
    glVertex2f(1014, 172) #K_15
    glVertex2f(1016, 163) #L_15
    glVertex2f(1017, 152) #M_15
    glVertex2f(1019, 128) #N_15
    glEnd()

    #Telinga Kanan8
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(1032, 128) #O_15
    glVertex2f(1035, 163) #P_15
    glVertex2f(1037, 174) #Q_15
    glVertex2f(1041, 181) #R_15
    glVertex2f(1049, 187) #S_15
    glVertex2f(1058, 190) #T_15
    glVertex2f(1066, 190) #U_15
    glVertex2f(1072, 188) #V_15
    glVertex2f(1079, 184) #W_15
    glVertex2f(1085, 178) #Z_15
    glVertex2f(1088, 170) #A_16
    glVertex2f(1089, 163) #B_16
    glVertex2f(1088, 154) #C_16
    glVertex2f(1082, 138) #D_16
    glVertex2f(1072, 115) #E_16
    glEnd()

def Kelinci9():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah9
    glVertex2f(1258, 400) #O_20
    glVertex2f(1268, 410) #P_20
    glVertex2f(1281, 419) #Q_20
    glVertex2f(1296, 425) #R_20
    glVertex2f(1314, 428) #S_20
    glVertex2f(1336, 428) #T_20
    glVertex2f(1353, 424) #U_20
    glVertex2f(1368, 417) #V_20
    glVertex2f(1377, 412) #W_20
    glVertex2f(1387, 403) #Z_20
    glVertex2f(1394, 393) #A_21
    glVertex2f(1399, 381) #B_21
    glVertex2f(1400, 370) #C_21
    glVertex2f(1396, 356) #D_21
    glVertex2f(1388, 345) #E_21
    glVertex2f(1377, 335) #F_21
    glVertex2f(1362, 327) #G_21
    glVertex2f(1343, 321) #H_21
    glVertex2f(1326, 320) #I_21
    glVertex2f(1308, 321) #J_21
    glVertex2f(1289, 326) #K_21
    glVertex2f(1273, 335) #L_21
    glVertex2f(1261, 345) #M_21
    glVertex2f(1253, 358) #N_21
    glVertex2f(1250, 373) #O_21
    glVertex2f(1252, 387) #P_21
    glEnd()

    #Telinga Kiri9
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(1278, 416) #Q_21
    glVertex2f(1264, 450) #R_21
    glVertex2f(1262, 459) #S_21
    glVertex2f(1261, 468) #T_21
    glVertex2f(1265, 478) #U_21
    glVertex2f(1272, 486) #V_21
    glVertex2f(1280, 490) #W_21
    glVertex2f(1289, 491) #Z_21
    glVertex2f(1298, 489) #A_22
    glVertex2f(1304, 486) #B_22
    glVertex2f(1311, 480) #C_22
    glVertex2f(1315, 470) #D_22
    glVertex2f(1316, 456) #E_22
    glVertex2f(1318, 428) #F_22
    glEnd()

    #Telinga Kanan9
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(1332, 428) #G_22
    glVertex2f(1334, 465) #H_22
    glVertex2f(1337, 476) #I_22
    glVertex2f(1343, 484) #J_22
    glVertex2f(1354, 490) #K_22
    glVertex2f(1363, 491) #L_22
    glVertex2f(1372, 489) #M_22
    glVertex2f(1378, 485) #N_22
    glVertex2f(1385, 478) #O_22
    glVertex2f(1388, 472) #P_22
    glVertex2f(1389, 464) #Q_22
    glVertex2f(1388, 457) #R_22
    glVertex2f(1384, 444) #S_22
    glVertex2f(1371, 416) #T_22

    glEnd()

def Kelinci10():
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)

    #Wajah10
    glVertex2f(1258, 100) #F_16
    glVertex2f(1271, 112) #G_16
    glVertex2f(1283, 119) #H_16
    glVertex2f(1301, 125) #I_16
    glVertex2f(1313, 127) #J_16
    glVertex2f(1335, 127) #K_16
    glVertex2f(1352, 123) #L_16
    glVertex2f(1367, 118) #M_16
    glVertex2f(1377, 112) #N_16
    glVertex2f(1388, 102) #O_16
    glVertex2f(1396, 90) #P_16
    glVertex2f(1399, 77) #Q_16
    glVertex2f(1398, 65) #R_16
    glVertex2f(1393, 52) #S_16
    glVertex2f(1385, 42) #T_16
    glVertex2f(1368, 29) #U_16
    glVertex2f(1350, 23) #V_16
    glVertex2f(1329, 19) #W_16
    glVertex2f(1304, 21) #Z_16
    glVertex2f(1283, 28) #A_17
    glVertex2f(1266, 39) #B_17
    glVertex2f(1255, 52) #C_17
    glVertex2f(1250, 70) #D_17
    glVertex2f(1251, 86) #E_17
    glEnd()

    #Telinga Kiri10
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(1278, 116) #F_17
    glVertex2f(1264, 150) #G_17
    glVertex2f(1261, 162) #H_17
    glVertex2f(1263, 174) #I_17
    glVertex2f(1269, 183) #J_17
    glVertex2f(1277, 188) #K_17
    glVertex2f(1286, 191) #L_17
    glVertex2f(1296, 189) #M_17
    glVertex2f(1304, 186) #N_17
    glVertex2f(1311, 178) #O_17
    glVertex2f(1314, 170) #P_17
    glVertex2f(1316, 157) #Q_17
    glVertex2f(1318, 127) #R_17
    glEnd()

    #Telinga Kanan10
    glBegin(GL_POLYGON)
    glColor3ub(160, 89, 201)
    glVertex2f(1332, 127) #S_17
    glVertex2f(1334, 163) #T_17
    glVertex2f(1336, 173) #U_17
    glVertex2f(1341, 182) #V_17
    glVertex2f(1350, 188) #W_17
    glVertex2f(1360, 190) #Z_17
    glVertex2f(1368, 190) #A_18
    glVertex2f(1376, 186) #B_18
    glVertex2f(1383, 180) #C_18
    glVertex2f(1388, 171) #D_18
    glVertex2f(1389, 162) #E_18
    glVertex2f(1386, 152) #F_18
    glVertex2f(1381, 137) #G_18
    glVertex2f(1371, 115) #H_18
    glEnd()

#Fungsi Ubah Warna Kelinci
def iniHandleMouse(button, state, x, y):
    global merah, hijau, biru
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah == 160 and hijau == 89 and biru == 201 :
            merah = randint (0, 255)
            hijau = randint (0, 255)
            biru = randint (0, 255)
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah == 160 and hijau == 89 and biru == 201 :
            merah = 252
            hijau = 3
            biru = 3
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

def timer(value):
    global angle_time
    if angle_time == 0:
        angle_time += 2
    else :
        angle_time -= 2
    glutTimerFunc(100, timer, 0)

#Fungsi Iterasi untuk looping keseluruhan program agar workspace tidak hilang tiba-tiba
def iterate():
    glViewport(25, 75, 500, 500) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1500, 0.0, 1500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #untuk membersihkan layar
    glLoadIdentity() #untuk mereset semua posisi grafik stsu bentuk
    iterate() #fungsi looping
    Kelinci1()
    Kelinci2()
    Kelinci3()
    Kelinci4()
    Kelinci5()
    Kelinci6()
    Kelinci7()
    Kelinci8()
    Kelinci9()
    Kelinci10()
    glutSwapBuffers() #untuk membersihkan layar


#Inisialisasi  
glutInit() #inilisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #mengatur layar supaya memunculkan warna 
glutInitWindowSize(900, 900) #untuk mengatur ukuran window
glutInitWindowPosition(250, 0) #untuk mengaatur posisi layar atau window untuk workspace 
wind = glutCreateWindow("Color Match lvl 2") #untuk memberi nama pada window
#timer(0)
glutDisplayFunc(showScreen) #untuk menampilkan object yang telah dibuat pada layar, fungsi callback
glutIdleFunc(showScreen) #membuat opengl terbuka dan menampilkan objek
glutMouseFunc(iniHandleMouse)
glutMainLoop() #untuk menilai segalanya dan untuk looping objek
