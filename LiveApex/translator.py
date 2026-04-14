### LiveApex Translator Functions ###
# These functions convert internal to common names or vice versa #

maps = {
    # BR Maps (Trios, Duos & Ranked)
    "mp_rr_canyonlands_hu_breach": "Kings Canyon",      # Season 28 Hardlight Addition
    "mp_rr_tropic_island_mu2_landscape": "Storm Point", # Season 25 Optimization
    "mp_rr_desertlands_hu_breach": "World's Edge",      # Season 28 Hardlight Addition
    "mp_rr_olympus_mu3": "Olympus",                     # Season 27 Map Update
    "mp_rr_divided_moon_mu1_breach": "Broken Moon",     # Season 28 Hardlight Addition
    "mp_rr_district_mu1_breach": "E-District",          # Season 28 Hardlight Addition
    # Wildcard Maps
    "mp_rr_canyonlands_hu_avt": "Kings Canyon (Wildcard)",
    # Mixtape Exclusive Maps
    "mp_rr_freedm_skulltown": "Skull Town"
    # Others (LTMs, etc.)
}

datacenters = {
    "ap-east-1": "Hong Kong",
    "ap-northeast-1": "Tokyo",
    "ap-southeast-1": "Singapore",
    "ap-southeast-2": "Sydney",
    "eu-central-1": "Frankfurt",
    "me-south-1": "Bahrain",
    "sa-east-1": "Sao Paolo",
    "us-east-1": "North Virginia",
    "us-east-2": "Ohio",
    "us-west-2": "Oregon",
}

### MISSING MELEE HEIRLOOM VARIANTS
weapons = {
    # GRENADES
    "mp_weapon_grenade_emp": "Arc Star",
    "mp_weapon_thermite_grenade": "Thermite Grenade",
    'mp_weapon_frag_grenade': "Frag Grenade",
    # AR WEAPONS
    "mp_weapon_energy_ar": "Havoc",
    "mp_weapon_vinson": "Flatline",
    "mp_weapon_nemesis": "Nemesis",
    "mp_weapon_rspn101": "R-301",
    "mp_weapon_hemlok": "Hemlok",
    # PISTOL WEAPONS
    "mp_weapon_semipistol": "P2020",
    "mp_weapon_wingman": "Wingman",
    "mp_weapon_autopistol": "RE-45",
    # LMG WEAPONS
    "mp_weapon_dragon_lmg": "Rampage",
    "mp_weapon_lmg": "Spitfire",
    "mp_weapon_esaw": "Devotion",
    "mp_weapon_lstar": "L-STAR",
    # SMG WEAPONS
    "mp_weapon_car": "Car",
    "mp_weapon_r97": "R-99",
    "mp_weapon_volt_smg": "Volt",
    "mp_weapon_pdw": "Prowler",
    'mp_weapon_alternator_smg': "Alternator",
    # SNIPER WEAPONS
    "mp_weapon_dmr": "Longbow",
    "mp_weapon_defender": "Charge Rifle",
    "mp_weapon_sentinel": "Sentinel",
    # MARKSMAN WEAPONS
    "mp_weapon_3030": "30-30",
    "mp_weapon_g2": "G7 Scout",
    "mp_weapon_doubletake": "Triple Take",
    # SHOTGUN WEAPONS
    "mp_weapon_energy_shotgun": "Peacekeeper",
    "mp_weapon_shotgun_pistol": "Mozambique",
    "mp_weapon_shotgun": "EVA-8",
    "mp_weapon_mastiff": "Mastiff",
    # CARE PACKAGE WEAPONS
    "mp_weapon_sniper": "Kraber",
    # OTHER WEAPONS
    "mp_weapon_bow": "Bocek",
    "mp_weapon_melee_survival": "Melee",
    'mp_weapon_mounted_turret_weapon': "Sheila (Placed)",
    'mp_weapon_mounted_turret_placeable': "Sheila (Mobile)"
}

## Common to Internal Names
map_untranslations = {
    "Kings Canyon": "mp_rr_canyonlands_hu",
    "Storm Point (Season 13)": "mp_rr_tropic_island_mu1",
    "Storm Point (Season 18)": "mp_rr_tropic_island_mu1_storm",
    "Storm Point (Season 21)": "mp_rr_tropic_island_mu2",
    "Storm Point": "mp_rr_tropic_island_mu2_landscape", # Season 25 optimization
    "Worlds Edge (Season 10)": "mp_rr_desertlands_mu3",
    "Worlds Edge (Season 16)": "mp_rr_desertlands_mu4",
    "Worlds Edge": "mp_rr_desertlands_hu",
    "Olympus": "mp_rr_olympus_mu2",
    "Broken Moon (Season 15)": "mp_rr_divided_moon",
    "Broken Moon": "mp_rr_divided_moon_mu1",
    "E-District": "mp_rr_district"
}

datacenter_untranslations = {
    "Hong Kong": "ap-east-1",
    "Tokyo": "ap-northeast-1",
    "Singapore": "ap-southeast-1",
    "Sydney": "ap-southeast-2",
    "Frankfurt": "eu-central-1",
    "Bahrain": "me-south-1",
    "Sao Paolo": "sa-east-1",
    "North Virginia": "us-east-1",
    "Ohio": "us-east-2",
    "Oregon": "us-west-2"
}

# MISSING MELEE HEIRLOOM VARIANTS
weapon_untranslations = {
    # GRENADES
    "Arc Star": "mp_weapon_grenade_emp",
    "Thermite Grenade": "mp_weapon_thermite_grenade",
    'Frag Grenade': 'mp_weapon_frag_grenade',
    # AR WEAPONS
    "Havoc": "mp_weapon_energy_ar",
    "Flatline": "mp_weapon_vinson",
    "Nemesis": "mp_weapon_nemesis",
    "R-301": "mp_weapon_rspn101",
    "Hemlok": "mp_weapon_hemlok",
    # PISTOL WEAPONS
    "P2020": "mp_weapon_semipistol",
    "Wingman": "mp_weapon_wingman",
    "RE-45": "mp_weapon_autopistol",
    # LMG WEAPONS
    "Rampage": "mp_weapon_dragon_lmg",
    "Spitfire": "mp_weapon_lmg",
    "Devotion": "mp_weapon_esaw",
    "L-STAR": "mp_weapon_lstar",
    # SMG WEAPONS
    "Car": 'mp_weapon_car',
    'R-99': 'mp_weapon_r97',
    'Volt': 'mp_weapon_volt_smg',
    'Prowler': 'mp_weapon_pdw',
    'Alternator': 'mp_weapon_alternator_smg',
    # SNIPER WEAPONS
    'Longbow': 'mp_weapon_dmr',
    'Charge Rifle': 'mp_weapon_defender',
    'Sentinel': 'mp_weapon_sentinel',
    # MARKSMAN WEAPONS
    '30-30': 'mp_weapon_3030',
    'G7 Scout': 'mp_weapon_g2',
    'Triple Take': 'mp_weapon_doubletake',
    # SHOTGUN WEAPONS
    'Peacekeeper': 'mp_weapon_energy_shotgun',
    'Mozambique Shotgun': 'mp_weapon_shotgun_pistol',
    'EVA-8': 'mp_weapon_shotgun',
    'Mastiff': 'mp_weapon_mastiff',
    # CARE PACKAGE WEAPONS
    'Kraber': 'mp_weapon_sniper',
    # OTHER WEAPONS
    'Bocek': 'mp_weapon_bow',
    'Melee': 'mp_weapon_melee_survival',
    'Sheila (Placed)': 'mp_weapon_mounted_turret_weapon',
    'Sheila (Mobile)': 'mp_weapon_mounted_turret_placeable'
}

class Translator:
    """
    # Translator

    This class contains functions to translate data from internal to common names.
    """

    def translateDatacenter(datacenter: str):
        """
        # Translate Datacenter

        Translates datacenter from internal reference to a common name or vice versa.

        ## Parameters

        :datacenter: The datacenter to translate. Either an internal or common name.

        ## Example

        ```python
        LiveApex.Translator.translateDatacenter('Sydney')
        ```

        ## Raises

        Exception: {datacenter} | If the datacenter parameter has no translations.
        """

        datacenter_lower = datacenter.lower()
        datacenters_lower = {k.lower(): v for k, v in datacenters.items()}
        datacenters_values_lower = {v.lower(): k for k, v in datacenters.items()}
        
        if datacenter_lower in datacenters_lower:
            return datacenters_lower[datacenter_lower]
        elif datacenter_lower in datacenters_values_lower:
            return datacenters_values_lower[datacenter_lower]
        else:
            raise Exception(f"Unknown datacenter: {datacenter}")

    def translateWeapon(weapon: str):
        """
        # Translate Weapon

        Translates weapon name from internal reference to a common name or vice versa.

        ## Parameters

        :weapon: The weapon to translate. Either an internal or common name.

        ## Example

        ```python
        LiveApex.Translator.translateWeapon('mp_weapon_melee_survival')
        ```

        ## Raises

        Exception: {weapon} | If the weapon parameter has no translations.
        """

        weapon_lower = weapon.lower()
        weapons_lower = {k.lower(): v for k, v in weapons.items()}
        weapons_values_lower = {v.lower(): k for k, v in weapons.items()}
        
        if weapon_lower in weapons_lower:
            return weapons_lower[weapon_lower]
        elif weapon_lower in weapons_values_lower:
            return weapons_values_lower[weapon_lower]
        else:
            raise Exception(f"Unknown weapon: {weapon}")

    def translateMap(map: str):
        """
        # Translate Map

        Translates map from internal reference to a common name or vice versa.

        ## Parameters

        :map: The map to translate. Either an internal or common name.

        ## Example

        ```python
        LiveApex.Translator.translateMap('mp_rr_tropic_island_mu2_landscape')
        ```

        ## Raises

        Exception: {map} | If the map parameter has no translations.
        """

        map_lower = map.lower()
        maps_lower = {k.lower(): v for k, v in maps.items()}
        maps_values_lower = {v.lower(): k for k, v in maps.items()}
        
        if map_lower in maps_lower:
            return maps_lower[map_lower]
        elif map_lower in maps_values_lower:
            return maps_values_lower[map_lower]
        else:
            raise Exception(f"Unknown map: {map}")
        
    def translatePlaylist(playlist: str, mode = None):
        """
        # Translate Playlist

        Translates playlist from internal reference to a common name or vice versa.

        ## Parameters

        :playlist: The map/playlist to translate. Either an internal playlist name or common map name.
        :mode: The gamemode of the playlist (required for translation to internal playlist name).

        ## Example

        ```python
        LiveApex.Translator.translatePlaylist('kings canyon', 'algs')
        ```

        ## Returns
        If translating from internal to common names, {map_name}:{mode_name}
        If translating from common to internal names, {internal_playlist_name}

        ## Raises

        Exception: {playlist} | If the playlist parameter has no translations.
        """

        if mode != None:
            playlist_key = f"{playlist}:{mode}".lower()
            playlists_lower = {k.lower(): v for k, v in playlists.items()}
            playlists_values_lower = {v.lower(): k for k, v in playlists.items()}
            
            if playlist_key in playlists_lower:
                return playlists_lower[playlist_key]
            elif playlist_key in playlists_values_lower:
                return playlists_values_lower[playlist_key]
            else:                
                raise Exception(f"Unknown playlist: {playlist}:{mode}")

        else:
            playlist_lower = playlist.lower()
            playlists_lower = {k.lower(): v for k, v in playlists.items()}
            playlists_values_lower = {v.lower(): k for k, v in playlists.items()}
            
            if playlist_lower in playlists_lower:
                return playlists_lower[playlist_lower]
            elif playlist_lower in playlists_values_lower:
                return playlists_values_lower[playlist_lower]
            else:
                raise Exception(f"Unknown playlist: {playlist}")