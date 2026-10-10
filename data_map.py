from dataclasses import dataclass


@dataclass
class ItemData:
    name: str
    type: str

DATA_MAP: dict[str, ItemData] = {
    "ADV_SCANNERS": ItemData("Adv Scanners", "Augment"),
    "ANTI_DRONE": ItemData("Anti-Combat Drone", "Drone"),  # Verified
    "AUTO_COOLDOWN": ItemData("Automated Re-loader", "Augment"),  # Verified
    "BACKUP_DNA": ItemData("Backup Dna", "Augment"),
    "BATTERY_BOOSTER": ItemData("Battery Booster", "Augment"),
    "BATTLE": ItemData("Combat I", "Drone"),  # Verified
    "BEAM_1": ItemData("Mini Beam", "Weapon"),  # Verified
    "BEAM_2": ItemData("Beam 2", "Weapon"),
    "BEAM_3": ItemData("Beam 3", "Weapon"),
    "BEAM_BIO": ItemData("Beam Bio", "Weapon"),
    "BEAM_FIRE": ItemData("Fire Beam", "Weapon"),  # Verified
    "BEAM_HULL": ItemData("Hull Beam", "Weapon"),  # Verified
    "BEAM_LONG": ItemData("Beam Long", "Weapon"),
    "BOARDER": ItemData("Boarding", "Drone"),  # Verified
    "BOARDER_ION": ItemData("Boarder Ion", "Weapon"),
    "BOMB_1": ItemData("Small Bomb", "Weapon"),  # Verified
    "BOMB_BREACH_1": ItemData("Bomb Breach 1", "Weapon"),
    "BOMB_BREACH_2": ItemData("Breach II", "Weapon"),  # Verified
    "BOMB_FIRE": ItemData("Bomb Fire", "Weapon"),
    "BOMB_HEAL": ItemData("Bomb Heal", "Weapon"),
    "BOMB_HEAL_SYSTEM": ItemData("Bomb Heal System", "Weapon"),
    "BOMB_ION": ItemData("Bomb Ion", "Weapon"),
    "BOMB_STUN": ItemData("Bomb Stun", "Weapon"),
    "CLOAK_FIRE": ItemData("Stealth Weapons", "Augment"),  # Verified
    "COMBAT_1": ItemData("Combat I", "Drone"),  # Verified
    "COMBAT_2": ItemData("Combat II", "Drone"),  # Verified
    "COMBAT_BEAM": ItemData("Combat Beam", "Weapon"),
    "COMBAT_BEAM_2": ItemData("Combat Beam 2", "Weapon"),
    "COMBAT_FIRE": ItemData("Combat Fire", "Drone"),
    "CREW_STIMS": ItemData("Mantis Pheromones", "Augment"),  # Verified
    "DEFENSE_1": ItemData("Defense I", "Drone"),  # Verified
    "DEFENSE_2": ItemData("Defense II", "Drone"),  # Verified
    "DRONE_RECOVERY": ItemData("Drone Recovery Arm", "Augment"),  # Verified
    "DRONE_SHIELD": ItemData("Drone Shield", "Drone"),
    "ENERGY_SHIELD": ItemData("Energy Shield", "Augment"),
    "EXPLOSIVE_REPLICATOR": ItemData("Explosive Replicator", "Augment"),
    "FEDERATION_BASE_ASSIST": ItemData("Federation Base Assist", "Weapon"),
    "FIRE_EXTINGUISHERS": ItemData("Fire Extinguishers", "Augment"),
    "FLEET_DISTRACTION": ItemData("Fleet Distraction", "Weapon"),
    "FTL_BOOSTER": ItemData("Ftl Booster", "Augment"),
    "FTL_JUMPER": ItemData("Adv. FTL Navigation", "Augment"),  # Verified
    "HIDDEN_FEDERATION_BASE_LIST": ItemData("Hidden Federation Base List", "Weapon"),
    "ION_1": ItemData("Ion 1", "Weapon"),
    "ION_2": ItemData("Ion 2", "Weapon"),
    "ION_4": ItemData("Ion 4", "Weapon"),
    "ION_ARMOR": ItemData("Reverse Ion Field", "Augment"),  # Verified
    "ION_CHAINGUN": ItemData("Chain Ion", "Weapon"),  # Verified
    "ION_CHARGEGUN": ItemData("Charge I.", "Weapon"),  # Verified
    "ION_STUN": ItemData("Ion Stun", "Weapon"),
    "LASER_BURST_1": ItemData("Basic Laser", "Weapon"),  # Verified
    "LASER_BURST_2": ItemData("Laser Burst 2", "Weapon"),
    "LASER_BURST_2_A": ItemData("Burst Laser I", "Weapon"),  # Verified
    "LASER_BURST_3": ItemData("Laser Burst 3", "Weapon"),
    "LASER_BURST_5": ItemData("Burst Laser III", "Weapon"),  # Verified
    "LASER_CHAINGUN": ItemData("Chain Laser", "Weapon"),  # Verified
    "LASER_CHAINGUN_2": ItemData("Laser Chaingun 2", "Weapon"),
    "LASER_CHARGEGUN": ItemData("Laser Chargegun", "Weapon"),
    "LASER_CHARGEGUN_2": ItemData("Laser Chargegun 2", "Weapon"),
    "LASER_HEAVY_1": ItemData("Heavy Laser I", "Weapon"),  # Verified
    "LASER_HEAVY_2": ItemData("Laser Heavy 2", "Weapon"),
    "LASER_HULL_1": ItemData("Laser Hull 1", "Weapon"),
    "LASER_HULL_2": ItemData("Laser Hull 2", "Weapon"),
    "LIFE_SCANNER": ItemData("Lifeform Scanner", "Augment"),  # Verified
    "MISSILES_1": ItemData("Missiles 1", "Weapon"),
    "MISSILES_2": ItemData("Hermes Missile", "Weapon"),  # Verified
    "MISSILES_2_PLAYER": ItemData("Missiles 2 Player", "Weapon"),
    "MISSILES_3": ItemData("Missiles 3", "Weapon"),
    "MISSILES_BREACH": ItemData("Missiles Breach", "Weapon"),
    "MISSILES_BURST": ItemData("Missiles Burst", "Weapon"),
    "MISSILES_HULL": ItemData("Missiles Hull", "Weapon"),
    "MISSILE_CHARGEGUN": ItemData("Missile Chargegun", "Weapon"),
    "NANO_MEDBAY": ItemData("Nano Medbay", "Augment"),
    "O2_MASKS": ItemData("O2 Masks", "Augment"),
    "REPAIR": ItemData("System Repair", "Drone"),  # Verified
    "REPAIR_ARM": ItemData("Repair Arm", "Augment"),  # Verified
    "ROCK_ARMOR": ItemData("Rock Plating", "Augment"),  # Verified
    "SCRAP_COLLECTOR": ItemData("Scrap Collector", "Augment"),
    "SHIELD_RECHARGE": ItemData("Shield Recharge", "Weapon"),
    "SHIP_REPAIR": ItemData("Hull Repair", "Drone"),  # Verified
    "SHOTGUN": ItemData("Flak I", "Weapon"),  # Verified
    "SHOTGUN_2": ItemData("Flak II", "Weapon"),  # Verified
    "SYSTEM_CASING": ItemData("System Casing", "Augment"),
    "TELEPORT_HEAL": ItemData("Teleport Heal", "Augment"),
    "WEAPON_PREIGNITE": ItemData("Weapon Pre-igniter", "Augment"),  # Verified
    "ZOLTAN_BYPASS": ItemData("Zoltan Shield Bypass", "Augment"),  # Verified
}
