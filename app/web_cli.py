from app import utils
from typing import Union


def parse_command(command: str) -> Union[str, dict]:
    """
    Parse CLI command and route to appropriate action
    :param command: Command string to parse
    :return: Response from parse as string or dict
    """
    command_original = command
    command = command.lower()

    # Dictionary of valid commands with key:value pairs
    valid_commands = {
        # Clear command
        'cls': 'clear',
        'clear': 'clear',
        # Help menu command
        'help': utils.read_from_file("static\\resources\\help_menu.html"),
        # Capture frame command
        'capture': 'capture',
        # Open code in IDE command
        'open': 'open',
        # List videos command
        'list-videos': list_videos(),
        # Available videos for autocomplete
        'available-videos': available_videos(),
        # Invalid play-video command
        'play-video': "<span class=\"text-red-500\">Invalid usage of play-video. Video must be specified. "
                "Type help for more information</span>"
    }

    result = valid_commands.get(command, None)

    if result is not None:
        return result

    # Multiple word/option commands
    return parse_split_command(command_original)


def parse_split_command(command_original: str) -> Union[str, dict]:
    """
    Parse multi option commands
    :param command_original: Command to parse
    :return: String or dict response to parse
    """
    split_commands = command_original.lower().split(" ")
    if len(split_commands) >= 2:
        # Navigate command
        if split_commands[0] == "navigate":
            available_pages = ["home", "upload", "collaborate", "settings"]
            if split_commands[1] in available_pages:
                if split_commands[1] == "home":
                    return {"redirect_page": "/"}
                return {"redirect_page": f"/{split_commands[1]}"}
        # Play video command
        if split_commands[0] == "play-video":
            play_filename = command_original[11:]
            if utils.filename_exists_in_userdata(play_filename):
                return {
                    "play_video": play_filename
                }
            return f"<span class=\"text-red-500\">Failed to open video \"{play_filename}\", file does not " \
                   "exist</span>"
    # Invalid command
    return f"<span class=\"text-red-500\">Invalid command \"{command_original}\", type help for more information</span>"


def available_videos() -> {}:
    """
    Returns dict of available videos to play
    :return: Dict containing video filenames
    """
    user_data = utils.read_user_data()
    if user_data is None:
        return {}
    all_videos = user_data["all_videos"]
    filename_dict = {}
    for index in range(0, len(all_videos)):
        filename_dict[index] = all_videos[index]["filename"]
    return filename_dict


def list_videos() -> str:
    """
    Returns formatted list of videos in users library
    :return: HTML formatted string of videos
    """

    user_data = utils.read_user_data()
    if user_data is None:
        return "<p class='text-red-500'>No videos found in your library.<p>"
    all_videos = user_data["all_videos"]
    formatted_video_string = "<pre><strong>Your Videos:</strong>"
    for current_video in all_videos:
        current_video_string = f"<br><p><strong>Filename: " \
                               f"</strong>{current_video['filename']}</p><p><strong>Duration: " \
                               f"</strong>{utils.format_timestamp(current_video['video_length'])}</p>"
        if current_video["progress"] != 0:
            current_video_string += f"<p><strong>Progress: " \
                                    f"</strong>{utils.format_timestamp(current_video['progress'])}</p>"
        capture_count = len(current_video["captures"])
        if capture_count > 0:
            current_video_string += f"<p><strong>Captures: </strong>{capture_count}</p>"
        formatted_video_string += current_video_string
    formatted_video_string += "</pre>"
    return formatted_video_string
