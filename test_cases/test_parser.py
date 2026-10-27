"""Regression checks against real FTL snapshots, including Stealth C equipment."""

import io
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import ftl_scum


FIXTURES = Path(__file__).parent
STEALTH_LOADOUT = (
    "Ship: Stealth C\n"
    "Sector: 8\n"
    "Weapons: Flak I, Mini Beam, Hull Laser I\n"
    "Drones: Shield Overcharger, Defense I, Combat I\n"
    "Augments: Long-Ranged Scanners, Weapon Pre-igniter\n"
    "Cargo: Laser Charger, Shield Overcharger, Hull Repair"
)


class ParserTests(unittest.TestCase):
    def test_stealth_c_loadout(self):
        self.assertEqual(
            ftl_scum.parse_save(str(FIXTURES / "test_case6.sav")), STEALTH_LOADOUT
        )

    def test_existing_loadouts(self):
        expected = {
            1: "Weapons: Flak II, Hull Beam, Basic Laser, Basic Laser\n"
               "Drones: Boarding, Defense II\n"
               "Augments: Stealth Weapons, Drone Recovery Arm, Repair Arm",
            2: "Weapons: Chain Laser, Burst Laser I\n"
               "Drones: Defense II\n"
               "Augments: Drone Recovery Arm, Weapon Pre-igniter",
            3: "Weapons: Burst Laser III, Flak I, Heavy Laser I\n"
               "Drones: Defense I, Combat I, Boarding\n"
               "Augments: Stealth Weapons\nCargo: Chain Ion",
            4: "Weapons: Small Bomb, Basic Laser\nAugments: Mantis Pheromones",
            5: "Weapons: Fire Beam, Flak I, Charge I., Breach II\n"
               "Drones: Defense I, Hull Repair\n"
               "Augments: Rock Plating, Weapon Pre-igniter, Zoltan Shield Bypass",
        }
        for number, equipment in expected.items():
            with self.subTest(snapshot=number):
                result = ftl_scum.parse_save(str(FIXTURES / f"test_case{number}.sav"))
                self.assertEqual("\n".join(result.splitlines()[2:]), equipment)

    def test_preview_refreshes_stale_details_and_preserves_metadata(self):
        metadata = (
            "Ship: Stealth C\nSector: 8\nWeapons: Old loadout\n"
            "Description: PostFight1\n\nSaved: 2026-10-27 17:52:04\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            save = Path(directory) / "snapshot.sav"
            shutil.copyfile(FIXTURES / "test_case6.sav", save)
            meta = Path(str(save) + ".meta")
            meta.write_text(metadata)
            output = io.StringIO()
            with patch.object(ftl_scum, "dest_dir", directory), redirect_stdout(output):
                ftl_scum.show_meta(save.name)
            preview = output.getvalue()
            self.assertIn(STEALTH_LOADOUT, preview)
            self.assertIn("Description: PostFight1\n\nSaved: 2026-10-27 17:52:04", preview)
            self.assertNotIn("Old loadout", preview)
            self.assertEqual(preview.count("Ship: "), 1)
            self.assertEqual(meta.read_text(), metadata)
            self.assertEqual(save.read_bytes(), (FIXTURES / "test_case6.sav").read_bytes())

    def test_preview_uses_metadata_when_snapshot_unavailable(self):
        with tempfile.TemporaryDirectory() as directory:
            metadata = "Ship: Kestrel A\nDescription: Backup\n"
            (Path(directory) / "missing.sav.meta").write_text(metadata)
            output = io.StringIO()
            with patch.object(ftl_scum, "dest_dir", directory), redirect_stdout(output):
                ftl_scum.show_meta("missing.sav")
            self.assertIn(metadata, output.getvalue())


if __name__ == "__main__":
    unittest.main()
