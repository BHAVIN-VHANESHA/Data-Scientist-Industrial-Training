# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# To update all the packages of python using pip on Windows and Linux System run the below command in terminal
nice python3 -m pip list --outdated --format=json | \ jq -r '.[] | "\(.name)==\(.latest_version)"' | \ xargs --no-run-if-empty -n1 pip3 install -U


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
