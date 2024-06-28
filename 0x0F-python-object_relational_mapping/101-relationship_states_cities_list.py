states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

        session.commit()
        