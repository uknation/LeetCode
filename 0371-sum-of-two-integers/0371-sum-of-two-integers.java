public class Sum_of_Two_Integers {

    public static void main(String[] args) {

        Sum_of_Two_Integers out = new Sum_of_Two_Integers();
//        System.out.println(out.getSum(1, 2)); // no carry

        // 2+2
        // recurion-1: sum=0, carry= (10)左移1位 =(100)=4
        // recursion-2: a=0,b=4
        // recursion-3: b=0
        System.out.println(out.getSum(2, 2)); // with carry
    }


    public int getSum(int a, int b) {
        if(b == 0){ // complete the operation when there is no carry
            return a;
        }

        int sum, carry;
        sum = a^b; // step-1 sum
        carry = (a&b)<<1; // step-2 sum

        return getSum(sum, carry);
    }
}

/////////

class Solution {
    public int getSum(int a, int b) {
        return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
    }
}