<!--Task 1 : There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with 
radius r2 and central coordinate (x2, y2)
Input numbers (real numbers) are separated by a space.
Write a PHP program to test the followings -
"C2 is in C1" if C2 is in C1
"C1 is in C2" if C1 is in C2
"Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect, 
and
"C1 and C2 do not overlap" if C1 and C2 do not overlap.-->

 <?php
$n = intval(fgets(STDIN));
for($i = 0; $i < $n; $i++){
    fscanf(STDIN, "%lf %lf %lf %lf %lf %lf", $xa, $ya, $ra, $xb, $yb, $rb);

    $r = sqrt(($xb - $xa)*($xb - $xa) + ($yb - $ya)*($yb - $ya));
    if($r + $ra < $rb){
        echo "C1  is in C2\n";
        continue;
    }
    if($r + $rb < $ra){
        echo "C2  is in C1.\n";
        continue;
    }

    if($r <= $ra + $rb){
        echo "Circumference of C1  and C2  intersect.";
        continue;
    }
    echo "C1 and C2 do not overlap.\n";
}
?>





<!--Task 2 :  Write a PHP program to compute the amount of the debt in n months. The -->
<!-- // borrowing amount is $100,000 and the loan adds 5% interest of the debt and  -->
<!-- // rounds it to the nearest 1,000 above month by month. -->
<!-- // Input: -->
<!-- // An integer n (0 = n = 100) . -->
<!-- Output: -->

<?php
function calculate_debt($a) {
    $debt = 100000;
    for ($i = 0; $i < $a; $i++) {
        $interest = $debt * 0.05;
        $debt += $interest;
        $debt = ceil($debt / 1000) * 1000; // Round up to nearest 1000
    }
    return $debt;
}
$a = 10000;
$finalDebt = calculate_debt($a);
echo "Total debt  $a: $finalDebt";
?>

<!--Task 3:  There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, 
ys). Write a PHP program to test whether AB and CD are orthogonal or not.
xp,yp, xq, yq, xr, yr, xs and ys are -100 to 100 respectively and each value can 
be up to 5 digits after the decimal point It is given as a real number including the 
number of.
 -->
<?php
define('EPS', 1e-8);
    $a = fscanf(STDIN, '%f %f %f %f %f %f %f %f');
    $line = array();
    $line[] = $a[1] - $a[3] === 0.0 ? INF : ($a[0] - $a[2]) / ($a[1] - $a[3]);
    $line[] = $a[5] - $a[7] === 0.0 ? INF : ($a[4] - $a[6]) / ($a[5] - $a[7]);
    if (max($line) === INF && min($line) === 0 || abs($line[0] * $line[1] + 1.0) < EPS) {
        echo 'Orthogonal';
    } else {
        echo 'Not orthogonal';
    }
    echo PHP_EOL;
?>
