# SmartStudy Integration Notes

This project currently ships with in-memory demo data and a mock chatbot. The UI is ready for database and chatbot integration through service/repository boundaries.

## Database

Repository contracts live in:

`src/smartstudy/data/repositories/contracts.py`

Current demo schedule storage:

`src/smartstudy/data/repositories/schedule_repo.py`

To connect a real database:

1. Create a new repository class, for example `SQLiteScheduleRepository`.
2. Implement the `ScheduleRepository` methods:
   - `list_events() -> list[Event]`
   - `add_event(event: Event) -> None`
3. Pass that repository into `ScheduleService(repository=...)` in `src/smartstudy/app.py`.

The UI should not call database code directly. Keep database access inside repositories and keep validation/business rules inside services.

## Chatbot

The chatbot boundary is:

`src/smartstudy/services/assistant_service.py`

The UI calls:

- `send_message(message: str, context: dict | None = None) -> ChatMessage`
- `list_history() -> list[ChatMessage]`
- `clear_history() -> None`

To connect a real chatbot, replace `AssistantService._generate_reply()` with an HTTP/SDK call. Keep the public methods unchanged so `AssistantPage` does not need to change.

Environment variables are documented in `.env.example`:

- `SMARTSTUDY_ASSISTANT_BASE_URL`
- `SMARTSTUDY_ASSISTANT_API_KEY`
- `SMARTSTUDY_ASSISTANT_MODEL`
- `SMARTSTUDY_DB_URL`

Do not commit real API keys.

## Data Models

Shared app models are in:

`src/smartstudy/core/models.py`

Important models:

- `Event`
- `Task`
- `Notification`
- `User`
- `ChatMessage`

If database schemas differ from these dataclasses, map database rows into these models inside the repository layer.

## Tests

Run:

```powershell
python -m unittest discover -s tests
```

The tests avoid importing UI classes where possible, so they can run without launching CustomTkinter windows.
