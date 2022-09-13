
def generateStruct():
    print()
    server_name = "unamed"
    password = "password"
    admin_password = ""
    enable_whitelist = bool
    check_players_client = bool
    disable_voice_chat = bool
    voice_chat_io_quality = int
    disable_tps = bool
    disable_crosshair = bool
    disable_personal_lighting = bool
    darker_night = bool  # lightingConfig
    server_time = str
    server_time_acceleration = int
    server_night_time_acceleration = float
    save_game_time = bool  # serverTimePersistent
    max_login_quene_players = int  # loginQueueMaxPlayers
    login_quene_players_concurents = int  # loginQueueConcurrentPlayers
    check_invalid_files = bool  # storageAutoFix
    respawn_time = int  # respawn time in seconds
    multithread_replication = bool  # multithreadedReplication
    mission_template = str