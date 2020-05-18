Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

isValidIP("0.0.0.0") ==> true
isValidIP("12.255.56.1") ==> true
isValidIP("137.255.156.100") ==> true
  
isValidIP('') ==> false
isValidIP('abc.def.ghi.jkl') ==> false
isValidIP('123.456.789.0') ==> false
isValidIP('12.34.56') ==> false
isValidIP('01.02.03.04') ==> false