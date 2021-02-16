from graphql import GraphQLError
import graphene
from .inter_layer import InterLayer, commit, register, login_required, Register
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphene import Schema


class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(UserType)

    @Register(commit('create_person_another_way'), login_required)
    def mutate(root, info, name):
        person = User.objects.create(username=name, password="123")
        ok = True
        return CreateUser(person=person, ok=ok)


class CreateUserWithEmail(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(UserType)

    @Register(commit('create_person_another_way'), login_required)
    def mutate(root, info, name):
        person = User.objects.create(username=name, password="123", email="test@test.com")
        ok = True
        return CreateUser(person=person, ok=ok)


class Mutaions(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_user_with_email = CreateUserWithEmail.Field()


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    @Register(commit("resolve_all_users"), login_required)
    def resolve_all_users(self, info):
        return User.objects.all()


schema = Schema(query=Query, mutation=Mutaions)

inter_schema = InterLayer(schema)
