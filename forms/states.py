from .base import State, Context

class CalculateTableState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We calculating table")
        context.set_state(None)


class AddDescriptionState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We are adding description")
        context.set_state(AddPayerState())


class AddPayersState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We are bill")
        context.set_state(CalculateTableState())


class AddBillState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We are bill")
        context.set_state(AddPayersState())


class AddPayerState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We are adding payer name")
        context.set_state(AddBillState())


class AddPaymentTimeState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We are adding time")
        context.set_state(AddDescriptionState())


class AddPaymentDateState(State):
    def is_valid(self, message):
        return True

    async def action_body(self, bot, message, context: Context) -> None:
        await bot.reply_to(message, "We are adding date")
        context.set_state(AddPaymentTimeState())
