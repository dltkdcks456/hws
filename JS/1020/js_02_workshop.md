# Workshop

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>

</head>

<body>
  <script>
    // 주어진 문자열이 회문인지 판별하는 isPalindrome 함수를 완성하시오.
    function isPalindrome(str) {
      const new_str = str.split(' ').join('')
      const arr = [...new_str]
      const reverseArr = arr.reverse()
      const reverseText = reverseArr.join('')
      if (new_str === reverseText) {
        return true
      } else {
        return false
      }
    }

    // 출력
    console.log(
      isPalindrome('a santa at nasa'),  // true
      isPalindrome('google')  // false
    )
  </script>
</body>

</html>
```

