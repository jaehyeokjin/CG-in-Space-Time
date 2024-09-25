set terminal wxt size 1350,1200 enhanced font 'Whitney,48' persist
set termoption enhanced
set encoding iso_8859_1
set xlabel 'Distance ({\305})'
set ylabel 'Pair Interaction (kcal/mol)'
set xr [4:16]
set yr [-1.5:3]
set ytics 1
set border lw 4
set key Left
y(x) = 4*1.19234899*((4.83/x)**12-(4.83/x)**6)
pl "A_A.table" u 2:3 w l lw 9 lc rgb '#FA8072' title 'Tail-Tail', "A_B.table" u 2:3 w l lw 9 lc rgb '#8A2BE2' title 'Center-Tail', "B_B.table" u 2:3 w l lw 9 lc rgb '#1e90ff' title 'Center-Ceneter', y(x) w l lw 7 dt '...' lc 'black' title 'Lewis–Wahnström'
