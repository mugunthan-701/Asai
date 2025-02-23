(* Define File Path for Gesture Input *)
slideFile = "E:\\DevFolioHack1\\slide.txt"; (* Ensure this path exists *)

(* Function to Start PowerPoint in Full-Screen Slide Show Mode *)
startPresentation[] := (
  Print["Starting PowerPoint in Full-Screen Mode..."];
  Run["powershell -Command \"Start-Process 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE' -ArgumentList '/s', 'E:\\DevFolioHack1\\Presentation.pptx'\""];
  Pause[5]; (* Wait for PowerPoint to fully load *)
  Print["PowerPoint Started in Full-Screen Slide Show Mode"];
);

(* Function to Move to Next Slide (Swipe Right) *)
nextSlide[] := (
  Print["Detected: SWIPE_RIGHT → Moving to Next Slide"];
  RunProcess[{"powershell", "-Command", 
    "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('{RIGHT}')"
  }];
);

(* Function to Move to Previous Slide (Swipe Left) *)
prevSlide[] := (
  Print["Detected: SWIPE_LEFT → Moving to Previous Slide"];
  RunProcess[{"powershell", "-Command", 
    "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('{LEFT}')"
  }];
);

(* Function to Close PowerPoint Properly *)


(* Initialize State *)
pptOpened = False;

(* Main Loop to Monitor slide.txt *)
While[True,
  If[FileExistsQ[slideFile],
    slideText = StringTrim[Import[slideFile, "Text"]];

    If[slideText === "OPEN_HAND",
      If[!pptOpened,
        Print["Detected: OPEN_HAND → Starting Presentation"];
        startPresentation[];
        pptOpened = True;
      ];
    ];

    If[slideText === "CLOSE_FIST",
      If[pptOpened,
        Print["Detected: CLOSE_FIST → Closing Presentation"];
        closePresentation[];
        pptOpened = False;
      ];
    ];

    If[slideText === "SWIPE_RIGHT", nextSlide[];];
    If[slideText === "SWIPE_LEFT", prevSlide[];];

  , Print["Error: slide.txt not found. Waiting..."];];

  Pause[0.5]; 
]
