map_translations = {
    "mp_rr_canyonlands_hu": "Kings Canyon (Season 14)",
    "mp_rr_tropic_island_mu1": "Storm Point (Season 13)",
    "mp_rr_tropic_island_mu1_storm": "Storm Point (Season 18)",
    "mp_rr_tropic_island_mu2": "Storm Point (Season 19)",
    "mp_rr_desertlands_mu3": "Worlds Edge (Season 10)",
    "mp_rr_desertlands_mu4": "Worlds Edge (Season 16)",
    "mp_rr_desertlands_hu": "Worlds Edge (Season 17)",
    "mp_rr_olympus_mu2": "Olympus (Season 12)",
    "mp_rr_divided_moon": "Broken Moon (Season 15)",
    "mp_rr_divided_moon_mu1": "Broken Moon (Season 21)",
    "mp_rr_district": "E-District (Season 22)",
}

ability_translations = {
    "": "",
    "": ""
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
    "mp_weapon_bow": "Bocek",
    # OTHER WEAPONS
    "mp_weapon_melee_survival": "Melee",
    'mp_weapon_mounted_turret_weapon': "Sheila (Mobile)",
    'mp_weapon_mounted_turret_placeable': "Sheila (Placed)"
}

class Translator:
    """
    # Translator

    This class contains functions to translate data from internal to common names.
    """

    def translateAbility(self, ability: str):
        """
        # Translate an Ability

        This function translates an ability from internal reference to a common name.

        ## Parameters

        :ability: The ability to translate.

        ## Example

        ```python
        LiveApexTranslator.translateAbility('')
        ```

        ## Raises
        
        Exception: {ability} | If the ability is unknown.
        """

        if ability in ability_translations:
            translated = ability_translations[ability]
        else:
            raise Exception(f"Unknown ability: {ability}")

        return translated
    
    def translateWeapon(self, weapon: str):
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

    def translateMap(self, map: str):
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