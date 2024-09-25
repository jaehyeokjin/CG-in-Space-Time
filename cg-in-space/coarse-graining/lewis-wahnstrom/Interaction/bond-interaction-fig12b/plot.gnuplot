set terminal wxt size 1350,1200 enhanced font 'Whitney,48' persist
set termoption enhanced
set encoding iso_8859_1
set xlabel 'Bond Distance ({\305})'
set ylabel 'Bonded Interaction (kcal/mol)'
set border lw 4
set xr [2:5.5]
set xtics format '%1.1f'
set yr [0:200]
set ytics 20
pl "A_B_bon.table" u 2:3 w l lw 9 lc rgb '#8a2be2' title 'Bond'
