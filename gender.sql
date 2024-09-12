IF INT(MID(STR([ID Number]), 7, 4)) < 5000 THEN
    "Female"
ELSE
    "Male"
END
