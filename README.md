# C115---Trabalho-final-Mininet


## 🧱 Etapa 1-a: Criar a topologia

```bash
sudo mn --topo tree,depth=4,fanout=3 --link tc,bw=35
```
```bash
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81 
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 
*** Adding links:
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s2) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s15) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s28) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s3) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s7) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s11) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s4) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s5) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s6) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h1) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h2) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h3) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h4) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h5) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h6) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h7) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h8) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h9) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s8) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s9) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s10) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h10) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h11) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h12) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h13) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h14) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h15) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h16) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h17) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h18) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s12) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s13) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s14) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h19) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h20) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h21) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h22) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h23) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h24) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h25) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h26) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h27) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s16) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s20) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s24) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s17) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s18) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s19) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h28) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h29) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h30) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h31) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h32) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h33) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h34) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h35) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h36) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s21) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s22) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s23) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h37) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h38) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h39) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h40) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h41) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h42) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h43) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h44) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h45) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s25) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s26) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s27) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h46) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h47) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h48) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h49) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h50) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h51) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h52) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h53) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h54) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s29) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s33) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s37) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s30) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s31) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s32) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h55) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h56) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h57) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h58) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h59) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h60) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h61) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h62) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h63) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s34) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s35) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s36) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h64) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h65) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h66) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h67) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h68) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h69) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h70) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h71) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h72) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s38) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s39) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s40) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h73) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h74) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h75) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h76) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h77) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h78) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h79) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h80) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h81) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81 
*** Starting controller
c0 
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
```


## ✅ Etapa 1-b: Inspecionar infos

```bash
mininet> nodes
available nodes are: 
c0 h1 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h2 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h3 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h4 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h5 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h6 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h7 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h8 h80 h81 h9 s1 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s2 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s3 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s4 s40 s5 s6 s7 s8 s9
```
```bash
mininet> net
h1 h1-eth0:s4-eth1
h2 h2-eth0:s4-eth2
h3 h3-eth0:s4-eth3
h4 h4-eth0:s5-eth1
h5 h5-eth0:s5-eth2
h6 h6-eth0:s5-eth3
h7 h7-eth0:s6-eth1
h8 h8-eth0:s6-eth2
h9 h9-eth0:s6-eth3
h10 h10-eth0:s8-eth1
h11 h11-eth0:s8-eth2
h12 h12-eth0:s8-eth3
h13 h13-eth0:s9-eth1
h14 h14-eth0:s9-eth2
h15 h15-eth0:s9-eth3
h16 h16-eth0:s10-eth1
h17 h17-eth0:s10-eth2
h18 h18-eth0:s10-eth3
h19 h19-eth0:s12-eth1
h20 h20-eth0:s12-eth2
h21 h21-eth0:s12-eth3
h22 h22-eth0:s13-eth1
h23 h23-eth0:s13-eth2
h24 h24-eth0:s13-eth3
h25 h25-eth0:s14-eth1
h26 h26-eth0:s14-eth2
h27 h27-eth0:s14-eth3
h28 h28-eth0:s17-eth1
h29 h29-eth0:s17-eth2
h30 h30-eth0:s17-eth3
h31 h31-eth0:s18-eth1
h32 h32-eth0:s18-eth2
h33 h33-eth0:s18-eth3
h34 h34-eth0:s19-eth1
h35 h35-eth0:s19-eth2
h36 h36-eth0:s19-eth3
h37 h37-eth0:s21-eth1
h38 h38-eth0:s21-eth2
h39 h39-eth0:s21-eth3
h40 h40-eth0:s22-eth1
h41 h41-eth0:s22-eth2
h42 h42-eth0:s22-eth3
h43 h43-eth0:s23-eth1
h44 h44-eth0:s23-eth2
h45 h45-eth0:s23-eth3
h46 h46-eth0:s25-eth1
h47 h47-eth0:s25-eth2
h48 h48-eth0:s25-eth3
h49 h49-eth0:s26-eth1
h50 h50-eth0:s26-eth2
h51 h51-eth0:s26-eth3
h52 h52-eth0:s27-eth1
h53 h53-eth0:s27-eth2
h54 h54-eth0:s27-eth3
h55 h55-eth0:s30-eth1
h56 h56-eth0:s30-eth2
h57 h57-eth0:s30-eth3
h58 h58-eth0:s31-eth1
h59 h59-eth0:s31-eth2
h60 h60-eth0:s31-eth3
h61 h61-eth0:s32-eth1
h62 h62-eth0:s32-eth2
h63 h63-eth0:s32-eth3
h64 h64-eth0:s34-eth1
h65 h65-eth0:s34-eth2
h66 h66-eth0:s34-eth3
h67 h67-eth0:s35-eth1
h68 h68-eth0:s35-eth2
h69 h69-eth0:s35-eth3
h70 h70-eth0:s36-eth1
h71 h71-eth0:s36-eth2
h72 h72-eth0:s36-eth3
h73 h73-eth0:s38-eth1
h74 h74-eth0:s38-eth2
h75 h75-eth0:s38-eth3
h76 h76-eth0:s39-eth1
h77 h77-eth0:s39-eth2
h78 h78-eth0:s39-eth3
h79 h79-eth0:s40-eth1
h80 h80-eth0:s40-eth2
h81 h81-eth0:s40-eth3
s1 lo:  s1-eth1:s2-eth4 s1-eth2:s15-eth4 s1-eth3:s28-eth4
s2 lo:  s2-eth1:s3-eth4 s2-eth2:s7-eth4 s2-eth3:s11-eth4 s2-eth4:s1-eth1
s3 lo:  s3-eth1:s4-eth4 s3-eth2:s5-eth4 s3-eth3:s6-eth4 s3-eth4:s2-eth1
s4 lo:  s4-eth1:h1-eth0 s4-eth2:h2-eth0 s4-eth3:h3-eth0 s4-eth4:s3-eth1
s5 lo:  s5-eth1:h4-eth0 s5-eth2:h5-eth0 s5-eth3:h6-eth0 s5-eth4:s3-eth2
s6 lo:  s6-eth1:h7-eth0 s6-eth2:h8-eth0 s6-eth3:h9-eth0 s6-eth4:s3-eth3
s7 lo:  s7-eth1:s8-eth4 s7-eth2:s9-eth4 s7-eth3:s10-eth4 s7-eth4:s2-eth2
s8 lo:  s8-eth1:h10-eth0 s8-eth2:h11-eth0 s8-eth3:h12-eth0 s8-eth4:s7-eth1
s9 lo:  s9-eth1:h13-eth0 s9-eth2:h14-eth0 s9-eth3:h15-eth0 s9-eth4:s7-eth2
s10 lo:  s10-eth1:h16-eth0 s10-eth2:h17-eth0 s10-eth3:h18-eth0 s10-eth4:s7-eth3
s11 lo:  s11-eth1:s12-eth4 s11-eth2:s13-eth4 s11-eth3:s14-eth4 s11-eth4:s2-eth3
s12 lo:  s12-eth1:h19-eth0 s12-eth2:h20-eth0 s12-eth3:h21-eth0 s12-eth4:s11-eth1
s13 lo:  s13-eth1:h22-eth0 s13-eth2:h23-eth0 s13-eth3:h24-eth0 s13-eth4:s11-eth2
s14 lo:  s14-eth1:h25-eth0 s14-eth2:h26-eth0 s14-eth3:h27-eth0 s14-eth4:s11-eth3
s15 lo:  s15-eth1:s16-eth4 s15-eth2:s20-eth4 s15-eth3:s24-eth4 s15-eth4:s1-eth2
s16 lo:  s16-eth1:s17-eth4 s16-eth2:s18-eth4 s16-eth3:s19-eth4 s16-eth4:s15-eth1
s17 lo:  s17-eth1:h28-eth0 s17-eth2:h29-eth0 s17-eth3:h30-eth0 s17-eth4:s16-eth1
s18 lo:  s18-eth1:h31-eth0 s18-eth2:h32-eth0 s18-eth3:h33-eth0 s18-eth4:s16-eth2
s19 lo:  s19-eth1:h34-eth0 s19-eth2:h35-eth0 s19-eth3:h36-eth0 s19-eth4:s16-eth3
s20 lo:  s20-eth1:s21-eth4 s20-eth2:s22-eth4 s20-eth3:s23-eth4 s20-eth4:s15-eth2
s21 lo:  s21-eth1:h37-eth0 s21-eth2:h38-eth0 s21-eth3:h39-eth0 s21-eth4:s20-eth1
s22 lo:  s22-eth1:h40-eth0 s22-eth2:h41-eth0 s22-eth3:h42-eth0 s22-eth4:s20-eth2
s23 lo:  s23-eth1:h43-eth0 s23-eth2:h44-eth0 s23-eth3:h45-eth0 s23-eth4:s20-eth3
s24 lo:  s24-eth1:s25-eth4 s24-eth2:s26-eth4 s24-eth3:s27-eth4 s24-eth4:s15-eth3
s25 lo:  s25-eth1:h46-eth0 s25-eth2:h47-eth0 s25-eth3:h48-eth0 s25-eth4:s24-eth1
s26 lo:  s26-eth1:h49-eth0 s26-eth2:h50-eth0 s26-eth3:h51-eth0 s26-eth4:s24-eth2
s27 lo:  s27-eth1:h52-eth0 s27-eth2:h53-eth0 s27-eth3:h54-eth0 s27-eth4:s24-eth3
s28 lo:  s28-eth1:s29-eth4 s28-eth2:s33-eth4 s28-eth3:s37-eth4 s28-eth4:s1-eth3
s29 lo:  s29-eth1:s30-eth4 s29-eth2:s31-eth4 s29-eth3:s32-eth4 s29-eth4:s28-eth1
s30 lo:  s30-eth1:h55-eth0 s30-eth2:h56-eth0 s30-eth3:h57-eth0 s30-eth4:s29-eth1
s31 lo:  s31-eth1:h58-eth0 s31-eth2:h59-eth0 s31-eth3:h60-eth0 s31-eth4:s29-eth2
s32 lo:  s32-eth1:h61-eth0 s32-eth2:h62-eth0 s32-eth3:h63-eth0 s32-eth4:s29-eth3
s33 lo:  s33-eth1:s34-eth4 s33-eth2:s35-eth4 s33-eth3:s36-eth4 s33-eth4:s28-eth2
s34 lo:  s34-eth1:h64-eth0 s34-eth2:h65-eth0 s34-eth3:h66-eth0 s34-eth4:s33-eth1
s35 lo:  s35-eth1:h67-eth0 s35-eth2:h68-eth0 s35-eth3:h69-eth0 s35-eth4:s33-eth2
s36 lo:  s36-eth1:h70-eth0 s36-eth2:h71-eth0 s36-eth3:h72-eth0 s36-eth4:s33-eth3
s37 lo:  s37-eth1:s38-eth4 s37-eth2:s39-eth4 s37-eth3:s40-eth4 s37-eth4:s28-eth3
s38 lo:  s38-eth1:h73-eth0 s38-eth2:h74-eth0 s38-eth3:h75-eth0 s38-eth4:s37-eth1
s39 lo:  s39-eth1:h76-eth0 s39-eth2:h77-eth0 s39-eth3:h78-eth0 s39-eth4:s37-eth2
s40 lo:  s40-eth1:h79-eth0 s40-eth2:h80-eth0 s40-eth3:h81-eth0 s40-eth4:s37-eth3
c0
```
```bash
mininet> dump
<Host h1: h1-eth0:10.0.0.1 pid=3912> 
<Host h2: h2-eth0:10.0.0.2 pid=3914> 
<Host h3: h3-eth0:10.0.0.3 pid=3916> 
<Host h4: h4-eth0:10.0.0.4 pid=3918> 
<Host h5: h5-eth0:10.0.0.5 pid=3920> 
<Host h6: h6-eth0:10.0.0.6 pid=3922> 
<Host h7: h7-eth0:10.0.0.7 pid=3924> 
<Host h8: h8-eth0:10.0.0.8 pid=3926> 
<Host h9: h9-eth0:10.0.0.9 pid=3928> 
<Host h10: h10-eth0:10.0.0.10 pid=3930> 
<Host h11: h11-eth0:10.0.0.11 pid=3932> 
<Host h12: h12-eth0:10.0.0.12 pid=3934> 
<Host h13: h13-eth0:10.0.0.13 pid=3936> 
<Host h14: h14-eth0:10.0.0.14 pid=3938> 
<Host h15: h15-eth0:10.0.0.15 pid=3940> 
<Host h16: h16-eth0:10.0.0.16 pid=3942> 
<Host h17: h17-eth0:10.0.0.17 pid=3944> 
<Host h18: h18-eth0:10.0.0.18 pid=3946> 
<Host h19: h19-eth0:10.0.0.19 pid=3948> 
<Host h20: h20-eth0:10.0.0.20 pid=3950> 
<Host h21: h21-eth0:10.0.0.21 pid=3952> 
<Host h22: h22-eth0:10.0.0.22 pid=3954> 
<Host h23: h23-eth0:10.0.0.23 pid=3956> 
<Host h24: h24-eth0:10.0.0.24 pid=3958> 
<Host h25: h25-eth0:10.0.0.25 pid=3960> 
<Host h26: h26-eth0:10.0.0.26 pid=3962> 
<Host h27: h27-eth0:10.0.0.27 pid=3964> 
<Host h28: h28-eth0:10.0.0.28 pid=3966> 
<Host h29: h29-eth0:10.0.0.29 pid=3968> 
<Host h30: h30-eth0:10.0.0.30 pid=3970> 
<Host h31: h31-eth0:10.0.0.31 pid=3972> 
<Host h32: h32-eth0:10.0.0.32 pid=3974> 
<Host h33: h33-eth0:10.0.0.33 pid=3976> 
<Host h34: h34-eth0:10.0.0.34 pid=3978> 
<Host h35: h35-eth0:10.0.0.35 pid=3980> 
<Host h36: h36-eth0:10.0.0.36 pid=3982> 
<Host h37: h37-eth0:10.0.0.37 pid=3984> 
<Host h38: h38-eth0:10.0.0.38 pid=3986> 
<Host h39: h39-eth0:10.0.0.39 pid=3988> 
<Host h40: h40-eth0:10.0.0.40 pid=3990> 
<Host h41: h41-eth0:10.0.0.41 pid=3992> 
<Host h42: h42-eth0:10.0.0.42 pid=3994> 
<Host h43: h43-eth0:10.0.0.43 pid=3996> 
<Host h44: h44-eth0:10.0.0.44 pid=3998> 
<Host h45: h45-eth0:10.0.0.45 pid=4000> 
<Host h46: h46-eth0:10.0.0.46 pid=4002> 
<Host h47: h47-eth0:10.0.0.47 pid=4004> 
<Host h48: h48-eth0:10.0.0.48 pid=4006> 
<Host h49: h49-eth0:10.0.0.49 pid=4008> 
<Host h50: h50-eth0:10.0.0.50 pid=4010> 
<Host h51: h51-eth0:10.0.0.51 pid=4012> 
<Host h52: h52-eth0:10.0.0.52 pid=4014> 
<Host h53: h53-eth0:10.0.0.53 pid=4016> 
<Host h54: h54-eth0:10.0.0.54 pid=4018> 
<Host h55: h55-eth0:10.0.0.55 pid=4020> 
<Host h56: h56-eth0:10.0.0.56 pid=4022> 
<Host h57: h57-eth0:10.0.0.57 pid=4024> 
<Host h58: h58-eth0:10.0.0.58 pid=4026> 
<Host h59: h59-eth0:10.0.0.59 pid=4028> 
<Host h60: h60-eth0:10.0.0.60 pid=4030> 
<Host h61: h61-eth0:10.0.0.61 pid=4032> 
<Host h62: h62-eth0:10.0.0.62 pid=4034> 
<Host h63: h63-eth0:10.0.0.63 pid=4036> 
<Host h64: h64-eth0:10.0.0.64 pid=4038> 
<Host h65: h65-eth0:10.0.0.65 pid=4040> 
<Host h66: h66-eth0:10.0.0.66 pid=4042> 
<Host h67: h67-eth0:10.0.0.67 pid=4044> 
<Host h68: h68-eth0:10.0.0.68 pid=4046> 
<Host h69: h69-eth0:10.0.0.69 pid=4048> 
<Host h70: h70-eth0:10.0.0.70 pid=4050> 
<Host h71: h71-eth0:10.0.0.71 pid=4052> 
<Host h72: h72-eth0:10.0.0.72 pid=4054> 
<Host h73: h73-eth0:10.0.0.73 pid=4056> 
<Host h74: h74-eth0:10.0.0.74 pid=4058> 
<Host h75: h75-eth0:10.0.0.75 pid=4060> 
<Host h76: h76-eth0:10.0.0.76 pid=4062> 
<Host h77: h77-eth0:10.0.0.77 pid=4064> 
<Host h78: h78-eth0:10.0.0.78 pid=4066> 
<Host h79: h79-eth0:10.0.0.79 pid=4068> 
<Host h80: h80-eth0:10.0.0.80 pid=4070> 
<Host h81: h81-eth0:10.0.0.81 pid=4072> 
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None,s1-eth3:None pid=4077> 
<OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None,s2-eth3:None,s2-eth4:None pid=4080> 
<OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None,s3-eth4:None pid=4083> 
<OVSSwitch s4: lo:127.0.0.1,s4-eth1:None,s4-eth2:None,s4-eth3:None,s4-eth4:None pid=4086> 
<OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None,s5-eth3:None,s5-eth4:None pid=4089> 
<OVSSwitch s6: lo:127.0.0.1,s6-eth1:None,s6-eth2:None,s6-eth3:None,s6-eth4:None pid=4092> 
<OVSSwitch s7: lo:127.0.0.1,s7-eth1:None,s7-eth2:None,s7-eth3:None,s7-eth4:None pid=4095> 
<OVSSwitch s8: lo:127.0.0.1,s8-eth1:None,s8-eth2:None,s8-eth3:None,s8-eth4:None pid=4098> 
<OVSSwitch s9: lo:127.0.0.1,s9-eth1:None,s9-eth2:None,s9-eth3:None,s9-eth4:None pid=4101> 
<OVSSwitch s10: lo:127.0.0.1,s10-eth1:None,s10-eth2:None,s10-eth3:None,s10-eth4:None pid=4104> 
<OVSSwitch s11: lo:127.0.0.1,s11-eth1:None,s11-eth2:None,s11-eth3:None,s11-eth4:None pid=4107> 
<OVSSwitch s12: lo:127.0.0.1,s12-eth1:None,s12-eth2:None,s12-eth3:None,s12-eth4:None pid=4110> 
<OVSSwitch s13: lo:127.0.0.1,s13-eth1:None,s13-eth2:None,s13-eth3:None,s13-eth4:None pid=4113> 
<OVSSwitch s14: lo:127.0.0.1,s14-eth1:None,s14-eth2:None,s14-eth3:None,s14-eth4:None pid=4116> 
<OVSSwitch s15: lo:127.0.0.1,s15-eth1:None,s15-eth2:None,s15-eth3:None,s15-eth4:None pid=4119> 
<OVSSwitch s16: lo:127.0.0.1,s16-eth1:None,s16-eth2:None,s16-eth3:None,s16-eth4:None pid=4122> 
<OVSSwitch s17: lo:127.0.0.1,s17-eth1:None,s17-eth2:None,s17-eth3:None,s17-eth4:None pid=4125> 
<OVSSwitch s18: lo:127.0.0.1,s18-eth1:None,s18-eth2:None,s18-eth3:None,s18-eth4:None pid=4128> 
<OVSSwitch s19: lo:127.0.0.1,s19-eth1:None,s19-eth2:None,s19-eth3:None,s19-eth4:None pid=4131> 
<OVSSwitch s20: lo:127.0.0.1,s20-eth1:None,s20-eth2:None,s20-eth3:None,s20-eth4:None pid=4134> 
<OVSSwitch s21: lo:127.0.0.1,s21-eth1:None,s21-eth2:None,s21-eth3:None,s21-eth4:None pid=4137> 
<OVSSwitch s22: lo:127.0.0.1,s22-eth1:None,s22-eth2:None,s22-eth3:None,s22-eth4:None pid=4140> 
<OVSSwitch s23: lo:127.0.0.1,s23-eth1:None,s23-eth2:None,s23-eth3:None,s23-eth4:None pid=4143> 
<OVSSwitch s24: lo:127.0.0.1,s24-eth1:None,s24-eth2:None,s24-eth3:None,s24-eth4:None pid=4146> 
<OVSSwitch s25: lo:127.0.0.1,s25-eth1:None,s25-eth2:None,s25-eth3:None,s25-eth4:None pid=4149> 
<OVSSwitch s26: lo:127.0.0.1,s26-eth1:None,s26-eth2:None,s26-eth3:None,s26-eth4:None pid=4152> 
<OVSSwitch s27: lo:127.0.0.1,s27-eth1:None,s27-eth2:None,s27-eth3:None,s27-eth4:None pid=4155> 
<OVSSwitch s28: lo:127.0.0.1,s28-eth1:None,s28-eth2:None,s28-eth3:None,s28-eth4:None pid=4158> 
<OVSSwitch s29: lo:127.0.0.1,s29-eth1:None,s29-eth2:None,s29-eth3:None,s29-eth4:None pid=4161> 
<OVSSwitch s30: lo:127.0.0.1,s30-eth1:None,s30-eth2:None,s30-eth3:None,s30-eth4:None pid=4164> 
<OVSSwitch s31: lo:127.0.0.1,s31-eth1:None,s31-eth2:None,s31-eth3:None,s31-eth4:None pid=4167> 
<OVSSwitch s32: lo:127.0.0.1,s32-eth1:None,s32-eth2:None,s32-eth3:None,s32-eth4:None pid=4170> 
<OVSSwitch s33: lo:127.0.0.1,s33-eth1:None,s33-eth2:None,s33-eth3:None,s33-eth4:None pid=4173> 
<OVSSwitch s34: lo:127.0.0.1,s34-eth1:None,s34-eth2:None,s34-eth3:None,s34-eth4:None pid=4176> 
<OVSSwitch s35: lo:127.0.0.1,s35-eth1:None,s35-eth2:None,s35-eth3:None,s35-eth4:None pid=4179> 
<OVSSwitch s36: lo:127.0.0.1,s36-eth1:None,s36-eth2:None,s36-eth3:None,s36-eth4:None pid=4182> 
<OVSSwitch s37: lo:127.0.0.1,s37-eth1:None,s37-eth2:None,s37-eth3:None,s37-eth4:None pid=4185> 
<OVSSwitch s38: lo:127.0.0.1,s38-eth1:None,s38-eth2:None,s38-eth3:None,s38-eth4:None pid=4188> 
<OVSSwitch s39: lo:127.0.0.1,s39-eth1:None,s39-eth2:None,s39-eth3:None,s39-eth4:None pid=4191> 
<OVSSwitch s40: lo:127.0.0.1,s40-eth1:None,s40-eth2:None,s40-eth3:None,s40-eth4:None pid=4194> 
<OVSController c0: 127.0.0.1:6653 pid=3905> 
```
```bash
mininet> h1 ifconfig
h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::bcb7:48ff:fea9:bc05  prefixlen 64  scopeid 0x20<link>
        ether be:b7:48:a9:bc:05  txqueuelen 1000  (Ethernet)
        RX packets 23  bytes 2804 (2.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9  bytes 726 (726.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
```bash
mininet> h1 ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host proto kernel_lo 
       valid_lft forever preferred_lft forever
2: h1-eth0@if226: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb state UP group default qlen 1000
    link/ether be:b7:48:a9:bc:05 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.0.0.1/8 brd 10.255.255.255 scope global h1-eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::bcb7:48ff:fea9:bc05/64 scope link proto kernel_ll 
       valid_lft forever preferred_lft forever
```
```bash
mininet> h1 route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 h1-eth0
```
## ✅ Etapa 1-c: Desenho ilustrativo da topologia

    ![Topologia Árvore](imagens/topologia_arvore_mininet.png)



```bash

```
```bash

```
```bash

```