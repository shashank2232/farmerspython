from sqlalchemy import  text, func
from datetime import datetime, timedelta
from extensions import db
from models.schedule import Schedule
from models.farms import Farm
from mappers.schedule import ScheduleMapper

class ScheduleRepository:
    @staticmethod
    def get_schedules_due_for_today():
        try:
            today = datetime.today().date()
            schedules = db.session.query(Schedule).join(Farm).filter(
                func.DATE(Farm.sowing_date + text('INTERVAL \'1 day\' * schedules.days_after_sowing')) == today
            ).all()
            return [ScheduleMapper.to_dto(s) for s in schedules]
        except Exception as e:
            raise e

    @staticmethod
    def get_schedules_due_for_tomorrow():
        try:
            tomorrow = datetime.today().date() + timedelta(days=1)
            schedules = db.session.query(Schedule).join(Farm).filter(
                func.DATE(Farm.sowing_date + text('INTERVAL \'1 day\' * schedules.days_after_sowing')) == tomorrow
            ).all()
            return [ScheduleMapper.to_dto(s) for s in schedules]
        except Exception as e:
            raise e

    @staticmethod
    def create_schedule(days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id):
        try:
            schedule = Schedule(days_after_sowing=days_after_sowing, fertiliser=fertiliser, quantity=quantity, quantity_unit=quantity_unit, price_per_unit=price_per_unit, farm_id=farm_id)
            db.session.add(schedule)
            db.session.commit()
            return ScheduleMapper.to_dto(schedule)
        except Exception as e:
            raise e
    
    @staticmethod
    def get_schedule_by_fertilizer(fertilizer_name):
        try:
            schedule = db.session.query(Schedule).filter_by(fertiliser=fertilizer_name).first()
            return ScheduleMapper.to_dto(schedule) if schedule else None
        except Exception as e:
            raise e
    
    @staticmethod
    def allSchedules():
        try:
            schedules = db.session.query(Schedule).all()
            return [ScheduleMapper.to_dto(s) for s in schedules]
        except Exception as e:
            raise e
        
    @staticmethod
    def update_schedule_by_id(id, days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id):
        try:
            schedule = Schedule.query.get(id)
            if not schedule:
                return None, "Schedule not found"

            schedule.days_after_sowing = days_after_sowing
            schedule.fertiliser = fertiliser
            schedule.quantity = quantity
            schedule.quantity_unit = quantity_unit
            schedule.price_per_unit = price_per_unit
            schedule.farm_id = farm_id

            db.session.commit()
            return ScheduleMapper.to_dto(schedule), None  # Return the DTO
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_schedule_by_id(id):
        try:
            schedule = Schedule.query.get(id)
            if not schedule:
                return {"message": "Schedule not found"}, 404

            db.session.delete(schedule)
            db.session.commit()
            return {"message": "Schedule deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            raise e
