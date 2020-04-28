# R 이론 및 실습

### Introduction to R

- AI도 데이터로 부터 학습함.
- 프로그래밍 언어들이 할 수 있는 것들이 비슷해져가고 있다.
  - Java로도 Python으로도 딥러닝 가능
- R은 Open source 프로그래밍 언어
- R은 interpreted language for interactive programming
  - Python도
  - interpreter vs compiler
    - 한줄한줄 vs 모든 명령어 수집 후 실행
    - 오류가 생기면 interpreter는 그 줄에서 멈춤
    - 속도는 compiler가 더 빠름
- 다른 언어와 연계할 수 있는 module이 있음. Python <=>R 가능
- R studio 라는 IDE를 시용...(integrated development environment) 집약된 개발 환경 툴
- 라이브러리 : 쓰고 싶은 모듈 찾기..
- https://www.r-bloggers.com/



### Basic Data Structure

- Homogeneous
  - 종류 하나
- Heterogeneous
  - 둘?

|      | Homogeneous   | Heterogenous |
| ---- | ------------- | ------------ |
| 1d   | Atomic vector | List         |
| 2d   | Matrix        | Dataframe    |
| nd   | Array         | Dataframe    |

```R
> A = c(1, 2, '3')
> A
[1] "1" "2" "3"
```

- R은 Python보다 데이터의 자유도가 낮다고 할수 있다. 

  - 위의 것만 봐도 '3'하나로 모두 character가 됨.

- Assignment Operator(<-, =)

  - A <- 1
  - A=1
  - 걍 A=1 쓰면될듯?

- Vector/Array

  - a = c(1,2,3) 

- Length:length(A)

- sum(A) : 합

- mean(A) : 평균

- A+1 하면 전체 1 더한 값 보여줌, 저장은 안되는듯?

  - 연산속도 빠른편

- A == 5 도 됨 마치 for문 돌린거처럼 

  ```R
  > A ==3
  [1] FALSE FALSE  TRUE FALSE
  ```

- 하나만 확인도 됨

  ```R
  > which(A==3)
  [1] 3
  > which(A==20)
  integer(0)
  ```

- #### which, length 활용 

  ```R
  > last_name = c('Lee','Kim',"Lee","choi")
  > last_name
  [1] "Lee"  "Kim"  "Lee"  "choi"
  > last_name=='Lee'
  [1]  TRUE FALSE  TRUE FALSE
  > which(last_name=='Lee')
  [1] 1 3
  > length(which(last_name=='Lee'))
  [1] 2
  ```

- #### List

  ```R
  > L = list(ids=1:5, whos=c('Kim','Lee','Choi'))
  > L
  $ids
  [1] 1 2 3 4 5
  
  $whos
  [1] "Kim"  "Lee"  "Choi"
  
  > L[1]
  $ids
  [1] 1 2 3 4 5
  
  > L[2]
  $whos
  [1] "Kim"  "Lee"  "Choi"
  
  > Lo = list(id=c(1,2,3,4,5))
  > Lo
  $id
  [1] 1 2 3 4 5
  
  > Lo = list(id=c(1,2,3,4,5), name=c('kim','lee'))
  > Lo
  $id
  [1] 1 2 3 4 5
  
  $name
  [1] "kim" "lee"
  
  > Lo[2]
  $name
  [1] "kim" "lee"
  
  > Lo[1]
  $id
  [1] 1 2 3 4 5
  
  > Lo[1][1]
  $id
  [1] 1 2 3 4 5
  
  > Lo[1][2]
  $<NA>
  NULL
  
  > Lo[2][1]
  $name
  [1] "kim" "lee"
  
  > Lo[2][1][1]
  $name
  [1] "kim" "lee"
  
  > Lo = list(name='Lee', phone='010-1234-5678')
  > Lo
  $name
  [1] "Lee"
  
  $phone
  [1] "010-1234-5678"
  ```

  ```R
  
  > person = list(name='lee', phone='010-000-0000')
  > person
  $name
  [1] "lee"
  
  $phone
  [1] "010-000-0000"
  
  > person2 = list(name='kim',phone='010-1234-5678')
  > person2
  $name
  [1] "kim"
  
  $phone
  [1] "010-1234-5678"
  
  > book = list(person, person2)
  > book
  [[1]]
  [[1]]$name
  [1] "lee"
  
  [[1]]$phone
  [1] "010-000-0000"
  
  
  [[2]]
  [[2]]$name
  [1] "kim"
  
  [[2]]$phone
  [1] "010-1234-5678"
  
  ```

  ```R
  > person
  $name
  [1] "lee"
  
  $phone
  [1] "010-000-0000"
  
  > person$name
  [1] "lee"
  
  > person$phone
  [1] "010-000-0000"
  
  > names(person)
  [1] "name"  "phone"
  ```

  ```R
  > length(book)
  [1] 2
  > book[[1]]
  $name
  [1] "lee"
  
  $phone
  [1] "010-000-0000"
  
  > book[1]
  [[1]]
  [[1]]$name
  [1] "lee"
  
  [[1]]$phone
  [1] "010-000-0000"
  
  
  > book[[1]]
  $name
  [1] "lee"
  
  $phone
  [1] "010-000-0000"
  
  > book[[2]]
  $name
  [1] "kim"
  
  $phone
  [1] "010-1234-5678"
  
  인덱스, 이름 둘다 접근 가능
  > person[[1]]
  [1] "lee"
  > person$name
  [1] "lee"
  
  기존 값에 추가 가능
  > person$age = 20
  > person
  $name
  [1] "lee"
  
  $phone
  [1] "010-000-0000"
  
  $age
  [1] 20
  ```

- #### data.frame

  - 2차원 구조, 행(rows, 세로)열(columns, 가로) 구조
  - 엑셀, csv 등 읽어와서 사용 가능
  - 주소록 만들기

  ```R
  > last_name = c('lee', 'park', 'kim')
  > age = c(20, 30, 40)
  > gender = c('M', 'F', 'M')
  > df = data.frame(last_name, age, gender)
  > df
    last_name age gender
  1       lee  20      M
  2      park  30      F
  3       kim  40      M
  
  array 3개 만든 것을 하나의 테이블(2차원 구조, 행열구조)에 합쳐줌(data.frame으로)
  
  > df[1]
    last_name
  1       lee
  2      park
  3       kim
  > df[[1]]
  [1] "lee"  "park" "kim" 
  > df[[1]][1]
  [1] "lee"
  
  추가 할 땐 list에 추가하듯이
  > phones = c('1111','2222','3333')
  > df$phone = phones
  > df
    last_name age gender phone
  1       lee  20      M  1111
  2      park  30      F  2222
  3       kim  40      M  3333
  
  지우기 
  > df$phone=NULL
  > df
    last_name age gender
  1       lee  20      M
  2      park  30      F
  3       kim  40      M
  
  인덱스로 접근하기
  > df[2,4]
  [1] "2222"
  
  > df[1,]
    last_name age gender phone
  1       lee  20      M  1111
  
  > df[1]
    last_name
  1       lee
  2      park
  3       kim
  
  > df[,]
    last_name age gender phone
  1       lee  20      M  1111
  2      park  30      F  2222
  3       kim  40      M  3333
  
  > df[2:3,]
    last_name age gender phone
  2      park  30      F  2222
  3       kim  40      M  3333
  
  > df[,2]
  [1] 20 30 40
  
  > df$gender
  [1] "M" "F" "M"
  
  > df$age = df$age+10
  
  > df
    last_name age gender phone
  1       lee  30      M  1111
  2      park  40      F  2222
  3       kim  50      M  3333
  
  > which(df$gender=='M')
  [1] 1 3
  > length(which(df$gender=='M'))
  [1] 2
  last_name이 park인 사람의 phone
  > df[which(df$last_name=='park'),]$phone
  [1] "2222"
  
  > df$age>35
  [1] FALSE  TRUE  TRUE
  
  > df[which(df$age>35),c('last_name','phone')]
    last_name phone
  2      park  2222
  3       kim  3333
  
  > df[,c('last_name','phone')]
    last_name phone
  1       lee  1111
  2      park  2222
  3       kim  3333
  
  > df[,c(1,2)]
    last_name age
  1       lee  30
  2      park  40
  3       kim  50
  
  > df[,c(1)]
  [1] "lee"  "park" "kim" 
  
  > df[,c(1,2)]
    last_name age
  1       lee  30
  2      park  40
  3       kim  50
  
  > df[,1]
  [1] "lee"  "park" "kim" 
  
  > df[1,]
    last_name age gender phone
  1       lee  30      M  1111
  
  > df[c(1,2),]
    last_name age gender phone
  1       lee  30      M  1111
  2      park  40      F  2222
  
  > df[1,2]
  [1] 30
  
  데이터 추가
  > d = c(a, 10, 20, 30)
  > d
  [1]  1  2  3 10 20 30
  
  데이터 보기
  View(df)
  ```

- #### Matrix

  - 행렬계산에 사용

  ```R
  3x4 matrix 만들기
  > matrix(1:12, nrow=3, byrow=FALSE)
       [,1] [,2] [,3] [,4]
  [1,]    1    4    7   10
  [2,]    2    5    8   11
  [3,]    3    6    9   12
  > 
  > matrix(1:12, nrow=3, byrow=TRUE)
       [,1] [,2] [,3] [,4]
  [1,]    1    2    3    4
  [2,]    5    6    7    8
  [3,]    9   10   11   12
  > A = matrix(1:12, nrow=3, byrow=TRUE)
  > 
  > A[2,3]
  [1] 7
  > 
  > A[1:2, 3:4]
       [,1] [,2]
  [1,]    3    4
  [2,]    7    8
  
  행렬바꾸기? 역행렬?
  > t(A)
       [,1] [,2] [,3]
  [1,]    1    5    9
  [2,]    2    6   10
  [3,]    3    7   11
  [4,]    4    8   12
  
  ```

- #### JSON

  - JASON : JavaScript Object Notation
  - syntax for storing and exchanging data
  - text, written with JavaScript object notation

  ```
  members -----name:'Lee'
  		  | age:35
  		  |
  		  --- name:'Kim'
  		  |    age:40
  		  |
  		  |
  		  --- name:'Smith'
  		 	  age:23
  ```

  - 사람들한테 공유하고 보여주기 위해.. 데이터를
  - 나는 R을 쓰지만 상대방은 다른 것을 쓸수 있기 때문에 함께 쓰기 위한 하나의 틀을 JSON으로 정했다고 생각하면 될듯



### R Programming

- #### Writing Data into a File

  - write.csv : export a data.frame into a file
    - write.csv(dataset, "filename.csv")

- #### Loading Data from a file

  - read.csv : reads a file in table format and creates a data frame from it, which cases corresponding to lines and variables to fields in the file

- #### Function

  ```R
  myfunction = function(arg1, arg2, ...) {
      
      statements
      
      return(object)
      
  }
  ```

  ```R
  > myfunc = function(a, b) {return (a+b)}
  > c = myfunc(1, 2)
  > c
  [1] 3
  
  > myfunc = function(a, b) {return (a*b)}
  > myfunc(10, 20)
  [1] 200
  ```

- #### Save

  - save : writes an external representation of R objects to the specified file

  ```R
  save(.., file='...')
  save.image(file='.Rdata')
  ```

### 

### Make data visible

- #### Plot

  ```R
  > a = c(1:10)
  > a
   [1]  1  2  3  4  5  6  7  8  9 10
  
  점으로 된 그래프
  > plot(a)
  
  선으로 된 그래프
  > plot(a, type='l')
  
  랜덤
  >rnorm(10) 
  
  > plot(rnorm(100), type='o')
  
  cex : 원 크기
  > plot(a, type='o', col = 'red', cex=10.0)
  ```

- #### ggplot2 

  ```R
  >library(ggplot2)
  
  >
  ```

- #### 3D Plot

  - install.packages('rgl')

- #### Map

  - ggmap, maps, mapdata, OpenStreetMap라는 library 있음



### Time Series Data Handling(시계열 데이터)

- #### Time Series Decomposition 



#### LaTeX

#### Sweave

###  

### 주소록 만들기

```r
>readline('블라블라')
#숫자로 바꾸기
>as.numeric(age)
# 글자로 바꾸기
>as.character(age)
#book이라는 dataframe에 new_item 추가하기
>rbind(book, new_item)

>for (i in 1:2) {
	내용    
}

>if (i==20){
    내용
}else {
    내용
}

while (TRUE) {
    내용,
    break 가능
}

#공백 제거
>name_list = paste('name-', ids, sep='')

# 그래프그리기
>plot()
>hist()

#1부터 10까지 중에 2개 뽑기
>sample(1:10, 2)

#중복 가능하게 하기
>sample(1:10, 20, replace=TRUE)

#크기 보기
> dim(book)
[1] 100   4
> nrow(book)
[1] 100
> ncol(book)
[1] 4
#표로 보기
> View(book)

#위에 몇개 아래 몇개 보기
>head(book, 숫자)
>tail(book, 숫자)

#나이 30넘는 사람 5개만 보여줘 위에서
>head(book[which(book$age>30),],5)
# 소득 1000 이하 5명
head(book[which(book$income<1000),],5)

#순서 알려주기
>order(book$income)

#소득순서로 book 보여줘
>book[order(book$income),]


>book[book$name=='name-10',]
#substring match 부분문자열 매칭
> book[which(grepl('5', book$name)),]
   id    name age income
5   5  name-5  26   4000
15 15 name-15  48    700
25 25 name-25  63   6500
35 35 name-35  34   1100
45 45 name-45  58   9500
50 50 name-50  42   4500
51 51 name-51  56   8900
52 52 name-52  13   5100
53 53 name-53  45   2100
54 54 name-54  61   6000
55 55 name-55  35   6800
56 56 name-56  13   4600
57 57 name-57  49    600
58 58 name-58  49    200
59 59 name-59  52   1600
65 65 name-65  58   4300
75 75 name-75  46   2500
85 85 name-85  47   6500
95 95 name-95  48   8500

> x = c('Lee', 'Choi', 'Park', 'Lea')
> grepl('e', x)
[1]  TRUE FALSE FALSE  TRUE

> library(rgl)
> points3d(book[,c('age','income','height')])
```



- #### Classification(분류)



### Making Applications

- 웹기반으로 개발
  - R Shiny 라는 패키지 이용
  - New Shiny Web Application



# ctrl shift c 주석

