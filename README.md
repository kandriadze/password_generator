# password_generator
დააააა შემდეგი დავალება პაროლებზეა:

1)უნდა შექმნა პაროლის დამგენერირებელი კლასი
2)მას უნდა გადაეცემოდეს კონსტრუქტორში კონფიგურაციის ფაილის PATH (კონფიგურაციის ფაილი არის JSON ან YAML ფორმატის რომელიც გინდა)
3)ცვლადებში, კლასის შიგნით, უნდა განთავსდეს შესაბამისი წაკითხული პარამეტრები კონფიგურაციის ფაილიდან (პაროლის სიგრძე, უნდა შეიცავდეს თუ არა ასევე რიცხვებს,
უნდა შეიცავდეს თუ არა სიმბოლოებს (მაგ ^&*@ და სხვა)
4)მთავარი ფუნქცია არის, რა თქმა უნდა, პაროლის დამგენერირებელი ფუნქცია, რომელიც სეტავს ამ კლასში, ცვლადში ამ პაროლის მნიშვნელობას
5)ჩატვირთე ამ დაგენერირებული პაროლის დაბეჭდვის ფუნქცია repr()-ში ანუ პაროლი უნდა დაიბეჭდოს repr()-ის გამოძახებით მხოლოდ (!!! არ დააბეჭდინო პაროლი თვითონ, დაბეჭდე მისი SHA-256 ჰეში)
6)ჩატვირთე ამ კლასის აღმწერი ფუნქცია str()-ში (ლოგიკურია, უნდა აღწეროს მიმდინარე მდგომარეობა ამ კლასის, კონფიგურაცია როგორია და და პაროლის დაგენერირება მოხდა თუ არა უკვე)
7)პაროლს როცა დააგენერირებ, ლინუქსის env variable-ად უნდა ჩასეტო სისტემაში(ჰეშირებული პაროლი, რა თქმა უნდა, SHA-256-ით)
8)კონფიგურაციის წაკითხვის და დაგენერირების მერე უნდა შემეძლოს ვიცოდე, ჩემი პაროლი ძლიერია თუ არა (ფუნქცია უნდა დაწერო, რომელიც ამას გეუბნება)
9)და ცოტა 'ხაკერული' თემა და ლოგიკურად მე-7 პუნქტის ნაწილი: სუსტია ის პაროლი, რომელის გატეხვაც შემიძლია, პირობითად 1 წუთზე ნაკლებ დროში), ამიტომ
ამ პუნქტში შენი დავალებაა, დაწერო მეორე კლასი, რომელიც ამ წინა კლასის მიერ დაგენერირებ პაროლს, ჩასეტილს env variable ლინუქსის სისტემაში, შეეცდება 'გატეხოს'
და თუ ვერ მოასწრო 1 წუთში, გაჩერდეს და თქვას, რომ ძლიერია, თუ არადა სუსტია
10) უცვლელი ბონუსი: შემოგვთავაზე რამე ახალი ფუნქცია, მინიმუმ ერთი მაინც...

მითითებები აქაც შედარებით თავისუფალია, მაგრამ სადაც წერია არის ზუსტად (მაგ. მე-2 პუნქტი, მაგ. ის, რომ ჰეშირებისთვის უნდა გამოიყენო SHA-256 და ა.შ)
სადაც არაა კონკრეტიკა, იქ შენს კრეატიულობას და წარმოსახვას ვენდობით

აბა, ისიამოვნე 😎
