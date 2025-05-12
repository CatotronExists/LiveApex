### LiveApex Translator Functions ###
# These functions convert internal to common names or vice versa #

## Internal to Common Names
map_translations = {
    "mp_rr_canyonlands_hu": "Kings Canyon",
    "mp_rr_tropic_island_mu1": "Storm Point (Season 13)",
    "mp_rr_tropic_island_mu1_storm": "Storm Point (Season 18)",
    "mp_rr_tropic_island_mu2": "Storm Point (Season 21)",
    "mp_rr_tropic_island_mu2_landscape": "Storm Point", # Season 25 optimization
    "mp_rr_desertlands_mu3": "Worlds Edge (Season 10)",
    "mp_rr_desertlands_mu4": "Worlds Edge (Season 16)",
    "mp_rr_desertlands_hu": "Worlds Edge",
    "mp_rr_olympus_mu2": "Olympus",
    "mp_rr_divided_moon": "Broken Moon (Season 15)",
    "mp_rr_divided_moon_mu1": "Broken Moon",
    "mp_rr_district": "E-District",
}

datacenter_translations = {
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
weapon_translations = {
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
    "mp_weapon_shotgun_pistol": "Mozambique Shotgun",
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
        # Translate a datacenter

        This function translates a datacenter from internal reference to a common name.

        ## Parameters

        :datacenter: The datacenter to translate.

        ## Example

        ```python
        LiveApex.Translator.translateDatacenter('')
        ```

        ## Raises

        Exception: {datacenter} | If the datacenter is unknown.
        """

        if datacenter in datacenter_translations:
            translated = datacenter_translations[datacenter]
        else:
            raise Exception(f"Unknown datacenter: {datacenter}")

        return translated

    def translateWeapon(weapon: str):
        """
        # Translate a Weapon

        This function translates a weapon from internal reference to a common name.

        ## Parameters

        :weapon: The weapon to translate.

        ## Example

        ```python
        LiveApex.Translator.translateWeapon('mp_weapon_melee_survival')
        ```

        ## Raises

        Exception: {weapon} | If the weapon is unknown.
        """

        if weapon in weapon_translations:
            translated = weapon_translations[weapon]
        else:
            raise Exception(f"Unknown weapon: {weapon}")

        return translated

    def translateMap(map: str):
        """
        # Translate a Map

        This function translates a map from internal reference to a common name.

        ## Parameters

        :map: The map to translate.

        ## Example

        ```python
        LiveApex.Translator.translateMap('mp_rr_tropic_island_mu2')
        ```

        ## Raises

        Exception: {map} | If the map is unknown.
        """

        if map in map_translations:
            translated = map_translations[map]
        else:
            raise Exception(f"Unknown map: {map}")

        return translated

    def untranslateDatacenter(datacenter: str):
        """
        # Untranslate a datacenter

        This function untranslates a datacenter from common name to internal reference.

        ## Parameters

        :datacenter: The datacenter to untranslate.

        ## Example

        ```python
        LiveApex.Translator.untranslateDatacenter('')
        ```

        ## Raises

        Exception: {datacenter} | If the datacenter is unknown.
        """

        if datacenter in datacenter_untranslations:
            translated = datacenter_untranslations[datacenter]
        else:
            raise Exception(f"Unknown datacenter: {datacenter}")

        return translated

    def untranslateWeapon(weapon: str):
        """
        # Untranslate a Weapon

        This function untranslates a weapon from common name to internal reference.

        ## Parameters

        :weapon: The weapon to untranslate.

        ## Example

        ```python
        LiveApex.Translator.untranslateWeapon('Mastiff')
        ```

        ## Raises

        Exception: {weapon} | If the weapon is unknown.
        """

        if weapon in weapon_untranslations:
            translated = weapon_untranslations[weapon]
        else:
            raise Exception(f"Unknown weapon: {weapon}")

        return translated

    def untranslateMap(map: str):
        """
        # Untranslate a Map

        This function untranslates a map from common name to internal reference.

        ## Parameters

        :map: The map to untranslate.

        ## Example

        ```python
        LiveApex.Translator.untranslateMap('Kings Canyon')
        ```

        ## Raises
        Exception: {map} | If the map is unknown.
        """

        if map in map_untranslations:
            translated = map_untranslations[map]
        else:
            raise Exception(f"Unknown map: {map}")

        return translated