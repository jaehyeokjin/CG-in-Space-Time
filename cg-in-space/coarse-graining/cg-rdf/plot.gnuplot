set terminal wxt size 1000,1200 enhanced font 'Whitney,40' persist
set border lw 4
set termoption enhanced
set encoding iso_8859_1
set xlabel 'Distance ({\305})'
set ylabel 'g_{COM} (R)'
set ytics format '%1.1f'
set yr [:2]
set ytics 0.5
set xr [2:16]
set key font ",36"

pl "1t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '380 K, {/Symbol r}=1.029 g/ml', "../ref-rdf/1t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "2t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '400 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/2t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "3t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '420 K, {/Symbol r}=0.999 g/ml', "../ref-rdf/3t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "4t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '440 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/4t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "5t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '450 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/5t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "6t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '460 K, {/Symbol r}=0.971 g/ml', "../ref-rdf/6t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "7t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '480 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/7t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "8t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '480 K, {/Symbol r}=0.957 g/ml', "../ref-rdf/8t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "9t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '500 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/9t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "10t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '500 K, {/Symbol r}=0.943 g/ml', "../ref-rdf/10t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "11t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/11t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "12t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=0.929 g/ml', "../ref-rdf/12t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "13t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=0.916 g/ml', "../ref-rdf/13t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "14t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.115 g/ml', "../ref-rdf/14t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "15t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/15t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "16t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.025 g/ml', "../ref-rdf/16t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "17t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.991 g/ml', "../ref-rdf/17t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "18t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.959 g/ml', "../ref-rdf/18t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "19t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.944 g/ml', "../ref-rdf/19t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "20t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.929 g/ml', "../ref-rdf/20t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "21t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.899 g/ml', "../ref-rdf/21t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "22t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.878 g/ml', "../ref-rdf/22t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'
pl "23t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '700 K, {/Symbol r}=1.069 g/ml', "../ref-rdf/23t.rdf" u 3:6 w l lw 7 dt '...' lc rgb '#1e90ff' title 'CG'

set terminal wxt size 1000,1200 enhanced font 'Whitney,42' persist
set border lw 4
set termoption enhanced
set encoding iso_8859_1
set xlabel 'Distance ({\305})'
set ylabel 'Pair Potential U(R) (kcal/mol)'
set xr [4:16]
set yr [-1:25]
pl "1t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '380 K, {/Symbol r}=1.029'
pl "2t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '400 K, {/Symbol r}=1.069'
pl "3t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '420 K, {/Symbol r}=0.999'
pl "4t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '440 K, {/Symbol r}=1.069'
pl "5t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '450 K, {/Symbol r}=1.069'
pl "6t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '460 K, {/Symbol r}=0.971'
pl "7t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '480 K, {/Symbol r}=1.069'
pl "8t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '480 K, {/Symbol r}=0.957'
pl "9t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '500 K, {/Symbol r}=1.069'
pl "10t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '500 K, {/Symbol r}=0.943'
pl "11t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=1.069'
pl "12t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=0.929'
pl "13t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=0.916'
pl "14t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.115'
pl "15t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.069'
pl "16t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.025'
pl "17t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.991'
pl "18t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.959'
pl "19t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.944'
pl "20t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.929'
pl "21t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.899'
pl "22t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.878'
pl "23t.rdf" u 3:6 w l lw 9 lc rgb '#FA8072' title '700 K, {/Symbol r}=1.069'
