def frame(text, char):
    assert len(text) != 0, 'The input array must not be empty!'
    width = max([len(i) for i in text])   # width
    box = f'{char}' * (width + 4) + '\n'    # Print box top row
    for item in text:
        if len(item) < width:
            box += f'{char} ' + item + (width - len(item)) * ' ' + f' {char}\n'
        else:
            box += f'{char} ' + item + f' {char}\n'
    box += f'{char}' * (width + 4)  # Print box bottom row
    return box


print(frame([' Create a frame!     ',
       '          __     __  ',
       '         /  \~~~/  \ ',
       '   ,----(     ..    )',
       '  /      \__     __/ ',
       ' /|         (\  |(   ',
       '^  \  /___\  /\ |    ',
       '   |__|   |__|-..    '],
      '*'))
print(frame(['Create','a','frame'], '*'))
print(frame(['Create','this','kata'], '+'))
print(frame(['Small', 'frame'], '~'))
print(frame(['This is a very long single frame'], '-'))

