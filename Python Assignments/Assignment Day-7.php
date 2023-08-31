<!--Task 2    Write a PHP program to compute the amount of the debt in n months. The -->
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
