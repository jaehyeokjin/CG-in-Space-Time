# GNUPLOT script for power spectrum (obtained from the 2PT simulation)
set terminal wxt size 1320,800 enhanced font 'Whitney,35' persist

set border lw 4
set termoption enhanced
set encoding iso_8859_1
set xlabel '{/Symbol n} (cm^{-1})'
set ylabel 'DoS: D({/Symbol n})'
set xr [:1200]
pl "aa/otp_nvt.100000000.2pt.mol.grps.pwr" every 3 u 1:10 w l lw 7 lc rgb '#FA8072' title 'All-Atom', "cg/mscg_nvt.100000.2pt.mol.grps.pwr" every 5 u 1:10 w l lw 7 lc rgb '#1E90FF' title 'CG'
