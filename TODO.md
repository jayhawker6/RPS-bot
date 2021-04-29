# ~~TODO:~~
## ~~Major:~~
- ~~Get a basic algorithm up and running~~
- ~~Find a decent way to integrate it into the framework~~

## ~~Minor:~~
- ~~IdiotProof program~~
    - ~~Find user input areas~~
        - ~~Idiotproof said areas using:~~
            - ```python
            while True:
                try:
                    response = input('Idiotproofed input goes here')
                except ValueError:
                    print('Do it right idiot!')
                    continue
                if response == x:
                    break
                elif response == y:
                    break
                else:
                    continue
