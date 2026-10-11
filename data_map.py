from dataclasses import dataclass


@dataclass
class ItemData:
    name: str
    type: str

DATA_MAP: dict[str, ItemData] = {
    "ADV_SCANNERS": ItemData("Long-Ranged Scanners", "Augment"),  # Verified
    "ANTI_DRONE": ItemData("Anti-Combat Drone", "Drone"),  # Verified
    "AUTO_COOLDOWN": ItemData("Automated Re-loader", "Augment"),  # Verified
    "BACKUP_DNA": ItemData("Backup DNA Bank", "Augment"),  # Verified
    "BATTERY_BOOSTER": ItemData("Battery Charger", "Augment"),  # Verified
    "BATTLE": ItemData("Combat I", "Drone"),  # Verified
    "BEAM_1": ItemData("Mini Beam", "Weapon"),  # Verified
    "BEAM_2": ItemData("Pike Beam", "Weapon"),  # Verified
    "BEAM_3": ItemData("Glaive Beam", "Weapon"),  # Verified
    "BEAM_BIO": ItemData("Anti-Bio Beam", "Weapon"),  # Verified
    "BEAM_FIRE": ItemData("Fire Beam", "Weapon"),  # Verified
    "BEAM_HULL": ItemData("Hull Beam", "Weapon"),  # Verified
    "BEAM_LONG": ItemData("Halberd Beam", "Weapon"),  # Verified
    "BOARDER": ItemData("Boarding", "Drone"),  # Verified
    "BOARDER_ION": ItemData("Ion Intruder", "Drone"),  # Verified
    "BOMB_1": ItemData("Small Bomb", "Weapon"),  # Verified
    "BOMB_BREACH_1": ItemData("Breach Bomb Mark I", "Weapon"),  # Verified
    "BOMB_BREACH_2": ItemData("Breach II", "Weapon"),  # Verified
    "BOMB_FIRE": ItemData("Fire Bomb", "Weapon"),  # Verified
    "BOMB_HEAL": ItemData("Healing Burst", "Weapon"),  # Verified
    "BOMB_HEAL_SYSTEM": ItemData("Repair Burst", "Weapon"),  # Verified
    "BOMB_ION": ItemData("Ion Bomb", "Weapon"),  # Verified
    "BOMB_STUN": ItemData("Stun Bomb", "Weapon"),  # Verified
    "CLOAK_FIRE": ItemData("Stealth Weapons", "Augment"),  # Verified
    "COMBAT_1": ItemData("Combat I", "Drone"),  # Verified
    "COMBAT_2": ItemData("Combat II", "Drone"),  # Verified
    "COMBAT_BEAM": ItemData("Anti-Ship Beam Drone I", "Drone"),  # Verified
    "COMBAT_BEAM_2": ItemData("Anti-Ship Beam Drone II", "Drone"),  # Verified
    "COMBAT_FIRE": ItemData("Fire Drone", "Drone"),  # Verified
    "CREW_STIMS": ItemData("Mantis Pheromones", "Augment"),  # Verified
    "DEFENSE_1": ItemData("Defense I", "Drone"),  # Verified
    "DEFENSE_2": ItemData("Defense II", "Drone"),  # Verified
    "DRONE_RECOVERY": ItemData("Drone Recovery Arm", "Augment"),  # Verified
    "DRONE_SHIELD": ItemData("Shield Overcharger", "Drone"),  # Verified
    "DEFENSE_SCRAMBLER": ItemData("Defense Scrambler", "Augment"),  # Verified
    "ENERGY_SHIELD": ItemData("Zoltan Shield", "Augment"),  # Verified
    "EXPLOSIVE_REPLICATOR": ItemData("Explosive Replicator", "Augment"),  # Verified
    "FEDERATION_BASE_ASSIST": ItemData("Federation Base Assist", "Event"),  # Verified
    "FIRE_EXTINGUISHERS": ItemData("Fire Suppression", "Augment"),  # Verified
    "FLEET_DISTRACTION": ItemData("Distraction Buoys", "Augment"),  # Verified
    "FTL_BOOSTER": ItemData("FTL Recharge Booster", "Augment"),  # Verified
    "FTL_JUMPER": ItemData("Adv. FTL Navigation", "Augment"),  # Verified
    "HIDDEN_FEDERATION_BASE_LIST": ItemData("Hidden Federation Base List", "Event"),  # Verified
    "ION_1": ItemData("Ion Blast I", "Weapon"),  # Verified
    "ION_2": ItemData("Ion Blast II", "Weapon"),  # Verified
    "ION_4": ItemData("Heavy Ion", "Weapon"),  # Verified
    "ION_ARMOR": ItemData("Reverse Ion Field", "Augment"),  # Verified
    "ION_CHAINGUN": ItemData("Chain Ion", "Weapon"),  # Verified
    "ION_CHARGEGUN": ItemData("Charge I.", "Weapon"),  # Verified
    "ION_STUN": ItemData("Stun Ion", "Weapon"),  # Verified
    "LASER_BURST_1": ItemData("Basic Laser", "Weapon"),  # Verified
    "LASER_BURST_2": ItemData("Dual Lasers", "Weapon"),  # Verified
    "LASER_BURST_2_A": ItemData("Burst Laser I", "Weapon"),  # Verified
    "LASER_BURST_3": ItemData("Burst Laser II", "Weapon"),  # Verified
    "LASER_BURST_5": ItemData("Burst Laser III", "Weapon"),  # Verified
    "LASER_CHAINGUN": ItemData("Chain Laser", "Weapon"),  # Verified
    "LASER_CHAINGUN_2": ItemData("Vulcan", "Weapon"),  # Verified
    "LASER_CHARGEGUN": ItemData("Charge Laser", "Weapon"),  # Verified
    "LASER_CHARGEGUN_2": ItemData("Charge Laser II", "Weapon"),  # Verified
    "LASER_HEAVY_1": ItemData("Heavy Laser I", "Weapon"),  # Verified
    "LASER_HEAVY_2": ItemData("Heavy Laser II", "Weapon"),  # Verified
    "LASER_HULL_1": ItemData("Hull Laser I", "Weapon"),  # Verified
    "LASER_HULL_2": ItemData("Hull Laser II", "Weapon"),  # Verified
    "LIFE_SCANNER": ItemData("Lifeform Scanner", "Augment"),  # Verified
    "MISSILES_1": ItemData("Leto Missile", "Weapon"),  # Verified
    "MISSILES_2": ItemData("Hermes Missile", "Weapon"),  # Verified
    "MISSILES_2_PLAYER": ItemData("Artemis Missile", "Weapon"),  # Verified
    "MISSILES_3": ItemData("Pegasus Missile", "Weapon"),  # Verified
    "MISSILES_BREACH": ItemData("Breach Missile", "Weapon"),  # Verified
    "MISSILES_BURST": ItemData("Swarm Missiles", "Weapon"),  # Verified
    "MISSILES_HULL": ItemData("Hull Missile", "Weapon"),  # Verified
    "MISSILE_CHARGEGUN": ItemData("Charge Missile", "Weapon"),  # Verified
    "NANO_MEDBAY": ItemData("Engi Med-bot Dispersal", "Augment"),  # Verified
    "O2_MASKS": ItemData("Emergency Respirators", "Augment"),  # Verified
    "REPAIR": ItemData("System Repair", "Drone"),  # Verified
    "REPAIR_ARM": ItemData("Repair Arm", "Augment"),  # Verified
    "ROCK_ARMOR": ItemData("Rock Plating", "Augment"),  # Verified
    "SCRAP_COLLECTOR": ItemData("Scrap Recovery Arm", "Augment"),  # Verified
    "SHIELD_RECHARGE": ItemData("Shield Charge Booster", "Augment"),  # Verified
    "SHIP_REPAIR": ItemData("Hull Repair", "Drone"),  # Verified
    "SHOTGUN": ItemData("Flak I", "Weapon"),  # Verified
    "SHOTGUN_2": ItemData("Flak II", "Weapon"),  # Verified
    "SHOTGUN_PLAYER": ItemData("Adv. Flak", "Weapon"),  # Verified
    "SYSTEM_CASING": ItemData("Titanium System Casing", "Augment"),  # Verified
    "TELEPORT_HEAL": ItemData("Reconstructive Teleport", "Augment"),  # Verified
    "WEAPON_PREIGNITE": ItemData("Weapon Pre-igniter", "Augment"),  # Verified
    "ZOLTAN_BYPASS": ItemData("Zoltan Shield Bypass", "Augment"),  # Verified
}
