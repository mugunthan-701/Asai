(* Ensure slide.txt exists *)
If[!FileExistsQ["slide.txt"], Export["slide.txt", "1", "Text"]];

(* Load Slide Images *)
slides = {"Slide1.jpg", "Slide2.jpg", "Slide3.jpg"};

(* Function to Read Slide Number with Error Handling *)
readSlide[] := Module[{num},
  num = ToExpression[Import["slide.txt", "Text"]];
  If[IntegerQ[num] && 1 <= num <= Length[slides], num, 1] (* Ensure valid slide number *)
];

(* Display Presentation *)
DynamicModule[{slide = readSlide[]},
  Column[{
    Style["Gesture-Controlled Presentation", Bold, 20],
    Dynamic[Import[slides[[readSlide[]]]]], (* Display slide dynamically *)
    Row[{
      Button["Previous", If[slide > 1, slide--; Export["slide.txt", ToString[slide], "Text"]]],
      Button["Next", If[slide < Length[slides], slide++; Export["slide.txt", ToString[slide], "Text"]]]
    }]
  }]
]