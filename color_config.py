def read_config():
    try:
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            primary_color = lines[0].strip()
            off_color = lines[1].strip()
            return primary_color, off_color
    except FileNotFoundError:
        # Default UVU colors if config file doesn't exist
        default_primary = '#4C721D'
        default_secondary = '#FFFFFF'
        return default_primary, default_secondary

def save_config(primary_color, off_color):
    with open('config.txt', 'w') as file:
        file.write(f"{primary_color}\n{off_color}")