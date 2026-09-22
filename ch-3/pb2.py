Letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''

print(Letter.replace("<|Name|>", "Muskan").replace("<|Date|>", "22/9/26"))