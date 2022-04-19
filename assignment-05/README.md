# [დავალება 5](https://classroom.btu.edu.ge/uploads/26/26696.pdf)

1. დაწერეთ პროგრამები boto3 მოდულის გამოყენებით რომ შექმნათ ლექციაში
   გამოყენებული რესურსები. პროექტს მოაყოლეთ მოკლე აღწერა თუ რომელი
   პროგრამა რას აკეთებს და როგორ უნდა გამოვიძახოთ. საჭირო რესურსები
   მითითებულია ლექციის ბოლოში. დავალება ატვირთეთ გითჰაბზე. დავალება
   ფასდება 10 ქულით. დავალების შესრულების საბოლოო თარიღია 23 აპრილი
   23:59. 24 აპრილიდან არ განახორციელოთ კომიტები რეპოზიტორიაზე.

## Instructions:

### <em> create_function</em> - takes 4 arguments

- function_name (string) : will be saved as provided name in aws
- iam_role (string) : aws role that should be assigned to lambda
- function_handler (string) : name of the provided lambda function
- zip_file (string) : path of a zip file which should be uploaded to aws

### <em> s3_trigger</em> - takes 2 arguments

- bucket_name (string) : name of the bucket which should have a trigger
- function_name (string) : lambda function which should run on an event
