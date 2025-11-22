import json
from pathlib import Path
from typing import Dict
from pydantic import BaseModel, Field, ValidationError, field_validator, computed_field

DB_FILE = Path("planetary_weights.json")

PLANETS = 
{
    "Mercury": 0.38, "Venus":   0.91, "Moon":   0.165, 
    "Mars": 0.38,    "Jupiter": 2.34, "Saturn": 0.93, 
    "Uranus": 0.92,  "Neptune": 1.12, "Pluto":  0.066
}


class UserWeights(BaseModel):
    """Model for a user's planetary weights."""
    name: str = Field(min_length=1, description="User's name")
    earth_weight: float = Field(gt=0, description="Weight on Earth in pounds")
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not empty and properly formatted."""
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip().title()
    
    @computed_field
    @property
    def planetary_weights(self) -> Dict[str, float]:
        """Auto-calculate planetary weights from earth_weight."""
        return {planet: self.earth_weight * factor 
                for planet, factor in PLANETS.items()}


class History(BaseModel):
    """Wrapper for all user weight history."""
    users: Dict[str, UserWeights] = Field(default_factory=dict)
    
    def add_user(self, user: UserWeights) -> None:
        """Add or update a user in history."""
        self.users[user.name] = user
    
    def get_user(self, name: str) -> UserWeights | None:
        """Get a user by name."""
        return self.users.get(name)
    
    def __len__(self) -> int:
        return len(self.users)
    
    def __iter__(self):
        return iter(self.users.values())


def input_float(prompt: str) -> float | None:
    """Get positive float or None."""
    while val := input(prompt).strip():
        try:
            if (num := float(val)) > 0:
                return num
            print("Must be > 0")
        except ValueError:
            print("Invalid number")
    return None


def load_data() -> History:
    """Load history, return empty History on error."""
    if not DB_FILE.exists():
        return History()
    
    try:
        data = json.loads(DB_FILE.read_text())
        return History(**data)
    except (json.JSONDecodeError, OSError, ValidationError) as e:
        print(f"Failed to load history: {e}")
        return History()


def save_data(history: History) -> None:
    """Save history with atomic write for robustness."""
    temp_file = DB_FILE.with_suffix('.tmp')
    try:
        # Write to temp file first
        temp_file.write_text(json.dumps(history.model_dump(), indent=2))
        temp_file.replace(DB_FILE)
    except OSError as e:
        print(f"Save failed: {e}")
        if temp_file.exists():
            temp_file.unlink()


def display(user: UserWeights) -> None:
    """Show weights."""
    print(f"\n{user.name}:")
    print("\n".join(f"  {p:<10} {w:>8.2f} lbs" 
                    for p, w in user.planetary_weights.items()))


def main() -> None:
    history = load_data()

    
    if len(history) > 0 and input("View history? (y/n): ").lower() == 'y':
        print("\n" + "="*50)
        for user in history:
            display(user)
        print("="*50)

    print("\nEnter name (press Enter to quit)")

  
    while name := input("\nName: ").strip().title():
        if history.get_user(name) and input(f"'{name}' exists. Overwrite? (y/n): ").lower() != 'y':
            continue

        if not (earth_weight := input_float("Weight (lbs): ")):
            continue

        try:
            user = UserWeights(name=name, earth_weight=earth_weight)
            history.add_user(user)
            display(user)
        except ValidationError as e:
            print(f"Validation failed: {e}")

    if len(history) > 0:
        save_data(history)
        print(f"\n✓ Saved {len(history)} entries")


if __name__ == "__main__":
    main()
    
    # -- Improvements --
                # - Error feedback
                # - History clarity
                # - Consistant formatting
