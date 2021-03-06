from abc import ABCMeta, abstractmethod

class Context:
    current_state = None

    def set_state(self, next_state) -> None:
        self.current_state = next_state

    async def action(self, bot, message) -> None:
        await self.current_state.action(bot, message, self)

class State(metaclass=ABCMeta):

    @abstractmethod
    def is_valid(self, message) -> str:
        ...

    async def action(self, bot, message, context: Context) -> None:
        validation_message = self.is_valid(message)
        if validation_message == None:
            await self.action_body(bot, message, context)
        else:
            await bot.reply_to(message, validation_message)

    @abstractmethod
    async def action_body(self, bot, message, context: Context) -> None:
        ...
