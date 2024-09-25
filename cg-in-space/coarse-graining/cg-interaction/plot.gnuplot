
set terminal wxt size 1000,1200 enhanced font 'Whitney,42' persist
set border lw 4
set termoption enhanced
set encoding iso_8859_1
set xlabel 'Distance ({\305})'
set ylabel 'Pair Potential U(R) (kcal/mol)'
set xr [4:16]
set yr [-1:25]
pl "1t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '380 K, {/Symbol r}=1.029'
pl "2t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '400 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "3t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '420 K, {/Symbol r}=0.999', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "4t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '440 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "5t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '450 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "6t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '460 K, {/Symbol r}=0.971', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "7t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '480 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "8t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '480 K, {/Symbol r}=0.957', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "9t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '500 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "10t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '500 K, {/Symbol r}=0.943', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "11t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "12t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=0.929', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "13t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '540 K, {/Symbol r}=0.916', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "14t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.115', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "15t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "16t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=1.025', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "17t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.991', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "18t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.959', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "19t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.944', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "20t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.929', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "21t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.899', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "22t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '600 K, {/Symbol r}=0.878', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
pl "23t.table" u 2:3 w l lw 9 lc rgb '#FA8072' title '700 K, {/Symbol r}=1.069', "1t.table" u 2:3 w l lw 7 lc rgb '#50c878' dt '...' notitle
